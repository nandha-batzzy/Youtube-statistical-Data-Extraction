from youtube_stats import YTstats

API_KEY = 'Add your Api Key'
channel_id = "Add the channel Id you need"
yt = YTstats(API_KEY,channel_id)
yt.get_channel_stats()
yt.get_vid_data()
yt.dump()