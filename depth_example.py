import pyzed.sl as sl

# Create a ZED camera object
zed = sl.Camera()

# Set configuration parameters
init_params = sl.InitParameters()
init_params.depth_mode = sl.DEPTH_MODE.ULTRA # Use ULTRA depth mode
init_params.coordinate_units = sl.UNIT.MILLIMETER # Use millimeter units (for depth measurements)

# Opens the ZED camera from the provided InitParameters and exits if it fails.
err = zed.open(init_params)
if (err != sl.ERROR_CODE.SUCCESS) :
    exit(-1)

# Grab an image
if zed.grab() ==  sl.ERROR_CODE.SUCCESS :
    # Create a matrix
    image = sl.Mat()
    # Get image from camera to matrix
    zed.retrieve_image(image, sl.VIEW.LEFT)  
    # Save image to filepath (replace <filepath> with wanted directory)
    image.write(r"<filepath>\leftImage.jpg")

    # Create an depth matrix 
    depth_map = sl.Mat()
    # Get depth map from camera to matrix (from left camera by default)
    zed.retrieve_image(depth_map, sl.VIEW.DEPTH)
    # Save depth map to filepath (replace <filepath> with wanted directory)
    depth_map.write(r"<filepath>\depthMap.jpg")	

zed.close()