import unittest
import youtube_dl


class facebookMetaData(unittest.TestCase):
    def test_likes_metadata(self):
        params = {}
        url = "https://www.facebook.com/iihfhockey/videos/2742345396033296/"
        ydl = youtube_dl.YoutubeDL(params)
        info = ydl.extract_info(url, download=False)
        self.assertGreater(info.get('like_count'), 200)

    def test_reactions_metadata(self):
        params = {}
        url = "https://www.facebook.com/supercarblondie/videos/519426815548240/"
        ydl = youtube_dl.YoutubeDL(params)
        info = ydl.extract_info(url, download=False)
        self.assertGreater(info.get('reactions_count'), 1000000)
        self.assertGreater(info.get('like_count'), 800000)

    def test_comments_live_video(self):
        params = {}
        url = "https://www.facebook.com/Medianetlive/videos/676754012901513/"
        ydl = youtube_dl.YoutubeDL(params)
        info = ydl.extract_info(url, download=False)
        self.assertGreater(info.get('comment_count'), 0)

    def test_metadata_fetch_with_log_in(self):
        url = "https://www.facebook.com/SerieA/videos/282581803097269"
        params = {}
        with open("cookie_file") as file:
            proxy = "ec2-3-221-82-67.compute-1.amazonaws.com:3128"
            params['cookiefile'] = file.name
            params['proxy'] = proxy
            ydl = youtube_dl.YoutubeDL(params)
            info = ydl.extract_info(url, download=False)
            self.assertTrue(info.get('timestamp'))
            self.assertTrue(info.get('view_count'))
            self.assertTrue(info.get('comment_count'))
            self.assertTrue(info.get('width'))
            self.assertTrue(info.get('uploader_id'))
            self.assertTrue(info.get('thumbnail'))


if __name__ == '__main__':
    unittest.main()
