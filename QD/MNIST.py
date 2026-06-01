import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.init as init
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.utils import make_grid
import matplotlib.pyplot as plt
import matplotlib as mpl


# Define Hyperparameters
num_epochs = 10
lr = 1e-3
batch_size = 10

# Data
# Download Data
mnist_train = dset.MNIST("./", train=True, transform=transforms.ToTensor(), target_transform=None, download=True)
mnist_test = dset.MNIST("./", train=False, transform=transforms.ToTensor(), target_transform=None, download=True)
mnist_train, mnist_val = torch.utils.data.random_split(mnist_train, [0.8, 0.2])

# Create Dataloader
dataloader = {}
dataloader['train'] = DataLoader(mnist_train, batch_size=batch_size, shuffle = True)
dataloader['test'] = DataLoader(mnist_test, batch_size=batch_size, shuffle = True)
dataloader['val'] = DataLoader(mnist_val, batch_size=batch_size, shuffle = True)

print(len(dataloader["train"]))

class VAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(28*28, 256),
            nn.ReLU()
        )

        self.fc_mu = nn.Linear(256, 10)
        self.fc_var = nn.Linear(256, 10)

        self.decoder = nn.Sequential(
            nn.Linear(10, 256),
            nn.ReLU(),
            nn.Linear(256, 28*28),
            nn.Sigmoid()
        )
    
    def encode(self, x):
        h = self.encoder(x)
        mu = self.fc_mu(h)
        log_var = self.fc_var(h)
        return mu, log_var
    
    def reparameterize(self, mu, log_var):
        std = torch.exp(log_var * 0.5)
        eps = torch.randn_like(std)
        return mu + std * eps

    def decode(self, z):
        recon = self.decoder(z)
        return recon
    
    def forward(self, x):
        batch_size = x.size(0)
        mu, log_var = self.encode(x.view(batch_size, -1))
        z = self.reparameterize(mu, log_var)
        out = self.decode(z)
        return out, mu, log_var
    
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
MSE = torch.nn.MSELoss(reduction='sum')

def loss_func(x, recon_x, mu, log_var):
    MSE_loss = MSE(recon_x, x.view(-1, 784))
    KL_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
    return MSE_loss + KL_loss

model = VAE().to(device)

optimiser = torch.optim.Adam(model.parameters(), lr = lr)

# Train
import time
import copy
def train_model(model, dataloader, criterion, optimiser, num_epochs=10):

    since = time.time()

    train_loss_history = []
    val_loss_history = []

    best_model_wts = copy.deepcopy(model.state_dict())
    best_val_loss = 100000000

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()
            
            else:
                model.eval()

            running_loss = 0.0

            for inputs, labels in dataloader[phase]:
                inputs = inputs.to(device)

                optimiser.zero_grad()

                with torch.set_grad_enabled(phase == 'train'):

                    outputs, mu, log_var = model(inputs)
                    loss = criterion(inputs, outputs, mu, log_var)  # calculate a loss


                    # backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()                             # perform back-propagation from the loss
                        optimiser.step()                             # perform gradient descent with given optimiser

                # statistics
                running_loss += loss.item()

            epoch_loss = running_loss / len(dataloader[phase].dataset)

            print('{} Loss: {:.4f}'.format(phase, epoch_loss))
            
            # deep copy the model
            if phase == 'train':
                train_loss_history.append(epoch_loss)

            if phase == 'val':
                val_loss_history.append(epoch_loss)

            if phase == 'val' and epoch_loss < best_val_loss:
                best_val_loss = epoch_loss
                best_model_wts = copy.deepcopy(model.state_dict())
            

        print()

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
    print('Best val Loss: {:4f}'.format(best_val_loss))

    # load best model weights
    model.load_state_dict(best_model_wts)
    return model, train_loss_history, val_loss_history
best_model, train_loss_history, val_loss_history = train_model(model, dataloader, loss_func, optimiser, num_epochs=num_epochs)

# Test
with torch.no_grad():
    running_loss = 0.0
    for inputs, labels in dataloaders["test"]:
        inputs = inputs.to(device)

        outputs, mu, log_var = best_model(inputs)
        test_loss = loss_func(inputs, outputs, mu, log_var)
        
        running_loss += test_loss.item()

    test_loss = running_loss / len(dataloaders["test"].dataset)
    print(test_loss)        
out_img = torch.squeeze(outputs.cpu().data)
print(out_img.size())