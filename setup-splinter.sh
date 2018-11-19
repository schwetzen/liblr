#!/usr/bin/env bash

source venv/bin/activate
PATH="$(pwd)/drivers:$PATH"
echo "Adding drivers/ directory to PATH..."
export PATH

# linux64/linux32/macos
platform=linux64
echo "Creating geckodriver symlink..."
cd drivers
rm geckodriver
ln -s geckodriver-${platform} geckodriver
cd ..

echo "Done."
