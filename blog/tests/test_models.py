from django.test import TestCase
from blog.models import Post

# Create your tests here.
class PostModelTest(TestCase):
    def test_is_empty(self):
        """初期状態で何も登録されていないことを確認
        """
        saved_posts = Post.objects.all()
        self.assertEqual(saved_posts.count(), 0)

    def test_is_count_one(self):
        """レコードを一つ作成すると正しく1つカウントされることを確認
        """
        post = Post(title='test_title', text='test_text')
        post.save()
        # レコードの全てを呼び出し
        saved_posts = Post.objects.all()
        self.assertEqual(saved_posts.count(), 1)

    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        post = Post()
        title = 'test_title_to_retrieve'
        text = 'test_text_to_retrieve'
        post.title = title
        post.text = text
        post.save()

        saved_posts = Post.objects.all()
        actual_post = saved_posts[0]

        self.assertEqual(actual_post.title, title)
        self.assertEqual(actual_post.text, text)