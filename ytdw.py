from pytube import YouTube 
  
#where to save 
SAVE_PATH = "/home/omparkash/youtube video download" #to_do 
  
#link of the video to be downloaded 
# link="https://www.youtube.com/watch?v=eaPag3Of8ZM"
link="https://www.youtube.com/watch?v=X1fqVZ4Vb8g"

yt = YouTube(link)  

try:
    print("downloading")
    yt.streams.filter(progressive = True, 
                    ).first().download(output_path = SAVE_PATH, 

                    # filename = "Reiner and Bertholdt Transformation scene")
                    )
    print('Task Completed!')
except:
    print("Some Error!")



