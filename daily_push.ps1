# Daily GitHub Push Script
# This script adds all changes, commits with a timestamped message, and pushes to origin main.

cd "c:\Users\E 555\Desktop\new_django\CSW2_blogapp"

# Add all changes
git add .

# Set a message with current date/time
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$message = "Daily update - $timestamp"

# Commit and Push
git commit -m $message
git push origin main

echo "Successfully pushed daily updates to GitHub at $timestamp"
