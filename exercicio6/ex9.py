#Use um dicionário onde valores são sets (ex.: tags: set de palavras-chave); adicione tags a um post e verifique overlaps com in e interseção.
posts = {
    "post1": {"python", "programação", "tutorial"},
    "post2": {"java", "programação", "desenvolvimento"}
}
tags = {"python", "web", "desenvolvimento"}
post = input("Digite o nome do post: ")
if post in posts:
    tags_post = posts[post]
    print(f"Tags do post: {tags_post}")
    if tags & tags_post:
        print("Há sobreposição de tags.")
    else:
        print("Não há sobreposição de tags.")
else:
    print(f"Post {post} não encontrado.")