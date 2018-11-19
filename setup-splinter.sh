#!/usr/bin/env bash

source venv/bin/activate
PATH="$(pwd)/drivers:$PATH"
echo "Adding drivers/ directory to PATH..."
export PATH

# linux64/linux32/macos
platform=linux64
echo "Creating geckodriver symlink..."
rm drivers/geckodriver
ln -s drivers/geckodriver-${platform} drivers/geckodriver

echo "Done."
