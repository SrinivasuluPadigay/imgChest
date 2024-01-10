# ImgChest and Reddit Image Posting Script

## Overview

This Python script automates the process of sharing images on [ImgChest](https://www.imgchest.com) and linking them on the [SauceSharingCommunity](https://www.reddit.com/r/SauceSharingCommunity/) subreddit. It was created by u/kei-kazuki (Srinivasulu Padigay) for u/DoujinStash.

## Functionality

1. **ImgChest Posting:**
   - The script reads images from the specified folder (`ToPostNext`).
   - It uploads each image to ImgChest, retrieves the direct image link, and obtains the ImgChest post ID.

2. **Reddit Posting:**
   - Using the obtained direct image link, the script makes a link submission to the SauceSharingCommunity subreddit on Reddit.
   - The script captures the Reddit post ID for future reference.

3. **Updating ImgChest Post:**
   - The ImgChest post's title is updated with a reference to the Reddit post ID for easy cross-referencing.

4. **Sleeping Periods:**
   - To avoid spam and adhere to subreddit rules, the script sleeps for a specified interval (default: 4 hours) between each post.
   - A buffer of 2 minutes is added to ensure that the time difference calculation is accurate.

## File Structure

- `imgChest.py`: The source code of the script.
- `ToPostNext/`: A folder containing images to be posted.

## Configuration

- `PAC`: Personal Access Token (Bearer Token) for ImgChest.
- Reddit API details:
  - `client_id`: Your Reddit app's client ID.
  - `client_secret`: Your Reddit app's client secret.
  - `password`: Your Reddit account password.
  - `user_agent`: A string identifying your application.
  - `username`: Your Reddit account username.

## Usage

1. Ensure you have the required libraries installed: `requests`, `time`, `praw`.
2. Set the ImgChest Personal Access Token (`PAC`) and Reddit API details.
3. Place images to be posted in the `ToPostNext` folder.
4. Run the script (`imgChest.py`).
5. The script will handle ImgChest and Reddit posting automatically.

## Important Notes

- Ensure that you adhere to the rules and guidelines of the SauceSharingCommunity subreddit.
- Regularly check and update the ImgChest Personal Access Token (`PAC`) to ensure uninterrupted service.

## Author

- **u/kei-kazuki (Srinivasulu Padigay)**

For any issues or inquiries, please contact u/kei-kazuki.

**Created for u/DoujinStash**
