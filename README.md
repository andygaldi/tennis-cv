# Description
Perform the following steps to run:
```
# Create and activate virtual env
pyenv install 3.10.4
pyenv virtualenv 3.10.4 tennis-cv
pyenv activate tennis-cv

# Install requirements
poetry install

# Set up gcloud config
gcloud config set account andy.galdi@gmail.com
gcloud config set project tennis-cv
export GOOGLE_APPLICATION_CREDENTIALS=~/personal/tennis-cv/key.json

# Need to do just once
SERVICE_ACCOUNT_NAME="tennis-cv"
PROJECT_ID=$(gcloud config get-value core/project)
SERVICE_ACCOUNT="$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com"
gcloud iam service-accounts keys create $GOOGLE_APPLICATION_CREDENTIALS \
  --iam-account $SERVICE_ACCOUNT
# Grant the service account the following roles: Service Usage Consumer and Storage Object Viewer

# Run code
python 2-determine-joints.py # Will do pose estimation on a video and calculate joint angles

# Cut video using CloudVisionAPI
# Track racquet and ball
# Determine contact point (and calculate joint angles at contact point)
# Repeat for other segments of swing
# Determine raquet speed (relative to max)
```

# Notes
Slow-Mo Video found here: https://www.youtube.com/@LoveTennisOfficial
Video Downloaded using this tool: https://youtubemp4.to/en27/
CloudVision API instructions: https://codelabs.developers.google.com/codelabs/cloud-video-intelligence-python3#0