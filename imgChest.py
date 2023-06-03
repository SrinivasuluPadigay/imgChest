"""
This program will do the following
    1. Make an image post in https://www.imgchest.com and get it's direct image link
    2. Make a link submission to https://www.reddit.com/r/SauceSharingCommunity/ with that direct image link
    3. Update title in https://www.imgchest.com with the reddit postID
    4. Sleep for 4 hours to avoid spam and follow r/SauceSharingCommunity rules

File Structure:
    imgChest.py     source program
    ToPostNext      folder containing images(specified folder)

Author: u/kei-kazuki (Srinivasulu Padigay)
Created for u/DoujinStash
"""

import os, requests, time, praw

FOLDER_NAME = "ToPostNext"
TIME_INTERVAL = 4 * 3600    # 4 hours in seconds
BUFFER = 120                # 2 minutes of buffer in seconds

# Personal Access Tokens (Bearer Token)
PAC = "PASTE_YOUR_PAC"

# Reddit objects
reddit = praw.Reddit(client_id="PASTE_YOUR_client_id",
                     client_secret="PASTE_YOUR_client_secret",
                     password="PASTE_YOUR_password",
                     user_agent="PASTE_YOUR_user_agent",
                     username="PASTE_YOUR_username")

def update_imgchest_post(redditPostID, imgChestPostID):
    title = f"Posted on https://www.reddit.com/r/SauceSharingCommunity | Sauce/Source at: https://redd.it/{redditPostID}"
    url = f"https://api.imgchest.com/v1/post/{imgChestPostID}"
    headers = {'Authorization': PAC}
    data = {'title': title}
    requests.put(url, headers=headers, data=data)

def upload_image_to_imgchest(image_path):
    url = "https://api.imgchest.com/v1/post"
    headers = {'Authorization': PAC}
    payload = {
        'privacy': 'public',
        'nsfw': 'true'}
    with open(image_path, 'rb') as file:
        files = {'images[]': file}
        response = requests.post(url, headers=headers, data=payload, files=files)
        jsonBody = response.json()
        return jsonBody['data']['id'], jsonBody['data']['images'][0]['link']

def getSleepTime():
    currentTime = float(time.time())
    latestPostTime = 1

    # Get u/DoujinStash last post's time to check if 4 hours is crossed or not
    user = reddit.redditor('DoujinStash')
    latestSubmission = user.submissions.new(limit=1)
    for post in latestSubmission:
        latestPostTime = float(post.created_utc)

    # Last posted time is > 4 hours then make post
    if (((currentTime - latestPostTime) / (60 * 60)) >= 4):
        sleepTime = 1
    else:
        sleepTime = round(latestPostTime + TIME_INTERVAL - currentTime) + BUFFER  # +120 seconds for butter

    return sleepTime

def main():
    # Read the folder and get the image
    for filename in os.listdir(FOLDER_NAME):
        time.sleep(getSleepTime())
        # Post the image to imgChest and get the direct image link to the image
        imgChestPostID, directImageLink = upload_image_to_imgchest(os.path.join(os.getcwd(),FOLDER_NAME, filename))
        print(f"Created post https://www.imgchest.com/p/{imgChestPostID}")
        # Post Image to Reddit and get Reddit post ID
        redditPostID = reddit.subreddit('SauceSharingCommunity').submit(title='Sauce please?',
                                                                        url=directImageLink,
                                                                        flair_id='0ede8f78-7fae-11ea-ab55-0ed45c340505')
        print(f"Created post https://redd.it/{redditPostID}")
        # Update the imgChest post title with Reddit Link for sauce reference
        update_imgchest_post(redditPostID, imgChestPostID)
        # Delete the image from the folder
        try:
            os.remove(os.path.join(FOLDER_NAME, filename))
        except Exception as e:
            msg = f"Failed to delete image.\nError = {e}\nFilename = {os.path.join(FOLDER_NAME, filename)}"
            reddit.redditor('kei-kazuki').message("DoujinStash: Failed to delete image", msg)

if __name__ == '__main__':
    main()