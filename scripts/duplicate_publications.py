from igreja.apps.blog.models import Post

publication_id = 1

post: Post = Post.objects.get(pk=publication_id)

for i, post in enumerate(Post.objects.all()):
    post.title = "Teste Titulo da Publicação " + str(i + 1)
    post.slug = "teste-titulo-da-publicacao-" + str(i + 1)
    post.save()

# for i in range(10):
#     d_post = post
#     d_post.id = None
#     d_post.title += f" {i}"
#     d_post.slug += f" {i}"

#     d_post.save()
