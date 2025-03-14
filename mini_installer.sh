echo "Downloading Miniconda installer..."
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda_installer.sh

# Make the installer executable
echo "Making the installer executable..."
chmod +x Miniconda_installer.sh

# Run the installer
echo "Running the Miniconda installer..."
./Miniconda_installer.sh -b -p $HOME/miniconda3


# chmod +x mini_installer.sh
