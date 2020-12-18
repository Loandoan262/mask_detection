# mask_detection
# 1. Open terminal. Go into the cloned project directory and type the following command:
```console
$ python train_3_lables.py --dataset dataset_akka
```
# 2. To detect face masks in an image type the following command:
```console
$ python detect_mask_image_akka.py --image images/akka_pic1.png
```
# 3. To detect face masks in real-time video streams type the following command:
```console
$ python detect_mask_video_akka.py 
```
# Test
![](https://github.com/Loandoan262/mask_detection/blob/main/video_mask_test.mp4)
<video controls="controls">
  <source type="video/mp4" src="video_mask_test.mp4"></source>
  <source type="video/webm" src="video_mask_test.webm"></source>
  <p>Your browser does not support the video element.</p>
</video>
