import requests

# Mapeamento de gêneros
GENEROS_TMDB = {
    28: "Ação", 12: "Aventura", 16: "Animação", 35: "Comédia", 80: "Crime",
    99: "Documentário", 18: "Drama", 10751: "Família", 14: "Fantasia",
    36: "História", 27: "Terror", 10402: "Música", 9648: "Mistério",
    10749: "Romance", 878: "Ficção Científica", 10770: "Cinema TV",
    53: "Thriller", 10752: "Guerra", 37: "Faroeste"
}

# 1. Nova função para ver filmes populares
def listar_filmes_populares():
    chave_api = "5dfc7c8c2095938c6ed4151d7807c523"
    url = "https://api.themoviedb.org/3/movie/popular"
    parametros = {"api_key": chave_api, "language": "pt-BR", "page": 1}

    try:
        resposta = requests.get(url, params=parametros, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        
        print("=== 🎬 Filmes Populares no TMDB ===")
        for filme in dados.get("results", [])[:10]:
            print(f"• {filme.get('title')}")
        print("=" * 35 + "\n")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao listar filmes: {e}\n")

# 2. Tua função de busca por nome
def buscar_filme():
    nome_filme = input("Digite o nome do filme: ").strip()
    if not nome_filme:
        print("\n❌ Por favor, digite um nome de filme válido.")
        return

    chave_api = "5dfc7c8c2095938c6ed4151d7807c523"
    url_api = "https://api.themoviedb.org/3/search/movie"
    parametros = {"api_key": chave_api, "query": nome_filme, "language": "pt-BR"}

    print("\nBuscando dados no TMDB...")

    try:
        resposta = requests.get(url_api, params=parametros, timeout=10)
        resposta.raise_for_status()
        dados_filme = resposta.json()
        resultados = dados_filme.get("results", [])

        if not resultados:
            print(f"\n❌ Nenhum filme foi encontrado com o termo '{nome_filme}'.")
            return

        filme = resultados[0]
        titulo_filme = filme.get("title", "Título indisponível")
        sinopse_filme = filme.get("overview", "Sinopse não informada.")
        avaliacao_filme = filme.get("vote_average", "N/A")
        ids_generos = filme.get("genre_ids", [])

        nomes_generos = [GENEROS_TMDB.get(id_genero, "Outro") for id_genero in ids_generos]
        generos_formatados = ", ".join(nomes_generos) if nomes_generos else "Gênero não informado"

        print("\n" + "=" * 50)
        print(f"🎬 Título: {titulo_filme}")
        print(f"🎭 Gênero(s): {generos_formatados}")
        print(f"⭐ Avaliação dos usuários: {avaliacao_filme}/10")
        print("-" * 50)
        print(f"📖 Sinopse:\n{sinopse_filme}")
        print("=" * 50)

    except requests.exceptions.RequestException as err:
        print(f"\n⚠️ Ocorreu uma falha na requisição: {err}")

# 3. Execução principal (chama primeiro os populares para sugestão e depois a busca)
if __name__ == "__main__":
    listar_filmes_populares()
    buscar_filme()