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

# Print serial number to prove it's working
zed_serial = zed.get_camera_information().serial_number
print("Hello! This is my serial number: ", zed_serial)	


zed.close()