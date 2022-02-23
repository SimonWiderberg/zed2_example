import pyzed.sl as sl

# Create a ZED camera object
zed = sl.Camera()

# Set configuration parameters
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD1080 
init_params.camera_fps = 30 

# Opens the ZED camera from the provided InitParameters and exits if it fails.
err = zed.open(init_params)
if (err != sl.ERROR_CODE.SUCCESS) :
    exit(-1)

# Grab an image
if (zed.grab() == sl.ERROR_CODE.SUCCESS) :
    # Create a matrix
    image = sl.Mat()
    # Get image from left camera to matrix
    zed.retrieve_image(image,sl.VIEW.LEFT) # Get the left image
    # Save image to filepath (replace <filepath> with wanted directory)
    image.write(r"<filepath>\leftImage.jpg")

zed.close()