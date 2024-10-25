import cv2
import os

"""
从视频中均匀采样指定数量的帧，并保存到输出目录中。
        
参数:
video_path: 视频文件的路径。
output_dir: 保存采样帧的输出目录。
num_samples: 需要采样的帧数量。
"""
def frame_sampling(base_path, output_dir, num_samples, start_index, end_index):

    for i in range(start_index, end_index + 1):
        # 生成文件名（例如：1.avi 到 16.avi）
        file_name = f"{i}.avi"
        file_path = os.path.join(base_path, file_name)

        if not os.path.exists(file_path):
            print(f"File does not exist: {file_path}")
            continue
        
        # 打开视频文件
        video_capture  = cv2.VideoCapture(file_path, cv2.CAP_MSMF)

        if not video_capture.isOpened():
            print(f"cant open video file path: {file_path}")
            continue
        
        print(f"processing video: {file_path}")
        # 获取视频的帧总数
        total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))    
        # 计算采样间隔
        interval = total_frames // num_samples
        # 确保输出目录存在
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        sampled_frame_count = 0
        frame_index = 0
        while video_capture.isOpened():
            ret, frame = video_capture.read()
        
            if not ret:
                break  # 读完视频结束
            
            # 如果当前帧是采样帧之一
            if frame_index % interval == 0:
                # 保存帧到输出目录
                frame_filename = os.path.join(output_dir, f"frame_{sampled_frame_count}.jpg")
                cv2.imwrite(frame_filename, frame)
                sampled_frame_count += 1
            
            frame_index += 1
            
            # 如果已经采样了足够的帧，停止
            if sampled_frame_count >= num_samples:
                break

        video_capture.release()
    
    cv2.destroyAllWindows()
    print("all videos are processed")


    
def main():
    # 定义视频的基础路径
    base_path = "D:\\Garrus\\Thesis\\Trail_camera_videos\\glazing_alone"

    output_dir = "D:\\Garrus\\Thesis\\Coding\\output_frames"

    num_samples = 10
    
    start_index = 1
    end_index = 16
    
    # 调用批量处理视频的函数
    frame_sampling(base_path, output_dir, num_samples, start_index, end_index)
def test():
    print(cv2.getBuildInformation())

if __name__ == "__main__":
    main()

