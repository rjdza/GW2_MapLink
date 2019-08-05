import mmap
import struct

last=[]
while True:
    shmem = mmap.mmap(0, 20, "MumbleLink", mmap.ACCESS_READ)
    coord=struct.unpack("IL3f", shmem)[2:5]

    shmem.close()
    if last!=coord:
        print(coord)
        last = coord
        X = coord[2]
        Y = coord[0]
        Z = coord[1]

s = struct.unpack('IL3f3f3f512s3f')
name = s[11].decode('utf-16')
camera_pos_x,camera_pos_y,camera_pos_z = s[12:15]