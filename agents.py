from crewai import Agent
from langchain.agents import load_tools

# Human Tools
human_tools = load_tools(["human"])


class YoutubeAutomationAgents():
    def youtube_manager(self):
        return Agent(
            role="YouTube Manager",
            goal="""
                    Supervisione o processo de preparação para o YouTube, incluindo pesquisa de mercado, idealização 
                    de título, descrição e criação de anúncio por e-mail necessários para fazer um vídeo do YouTube.
                 """,
            backstory="""
                    Como um gerente metódico e atento aos detalhes, você é responsável por supervisionar a preparação de vídeos 
                    para o YouTube. Ao criar vídeos para o YouTube, você segue o seguinte processo para criar um vídeo com altas 
                    chances de sucesso:
                1. Pesquise no YouTube para encontrar um mínimo de 15 outros vídeos sobre o mesmo tópico e analise seus títulos e descrições.
                2. Crie uma lista de 10 títulos potenciais que tenham menos de 70 caracteres e que devem possuir uma alta taxa de cliques.
                    -  Certifique-se de passar a lista de 1 vídeo para o criador de títulos para que ele possa usar as informações para 
                        criar os títulos.
                3.Escreva uma descrição para o vídeo do YouTube.
                4. Escreva um e-mail que pode ser enviado a todos os inscritos para promover o novo vídeo.
                """,
            allow_delegation=True,
            verbose=True,
        )

    def research_manager(self, youtube_video_search_tool, youtube_video_details_tool):
        return Agent(
            role="Gerente de Pesquisa do YouTube ",
            goal="""
                Para um determinado tópico e descrição de um novo vídeo do YouTube, encontre um mínimo de 15 vídeos de alto 
                desempenho sobre o mesmo tema com o objetivo final de preencher a tabela de pesquisa, que será usada por 
                outros agentes para ajudá-los a gerar títulos e outros aspectos do novo vídeo do YouTube que estamos 
                planejando criar.
                """,
            backstory="""Como um gerente de pesquisa metódico e detalhista, você é responsável por supervisionar pesquisadores 
                          que buscam ativamente no YouTube vídeos de alto desempenho sobre o mesmo tópico..""",
            verbose=True,
            allow_delegation=True,
            tools=[youtube_video_search_tool, youtube_video_details_tool]
        )

    def title_creator(self):
        return Agent(
            role="Criador de Títulos",
            goal="""Crie 10 títulos potenciais para um determinado tópico e descrição de vídeo do YouTube. Você também deve usar 
                    pesquisas anteriores para ajudar na geração dos títulos. Os títulos devem ter menos de 70 caracteres e ter alta taxa 
                    de cliques.""",
            backstory="""Como Criador de Títulos, você é responsável por criar 10 títulos potenciais para um determinado tópico 
                          e descrição de vídeo do YouTube..""",
            verbose=True
        )

    def description_creator(self):
        return Agent(
            role="Criador de Descrições",
            goal="""Crie uma descrição para um determinado tópico e descrição de vídeo do YouTube.""",
            backstory="""Como Criador de Descrições, você é responsável por criar uma descrição para um determinado tópico 
                          e descrição de vídeo do YouTube.""",
            verbose=True
        )

    def email_creator(self):
        return Agent(
            role="Criador de Email",
            goal="""Criar um e-mail para enviar à equipe de marketing para promover o novo vídeo do YouTube.""",
            backstory="""
                    Como Criador de E-mails, você é responsável por criar um e-mail para enviar à equipe de marketing 
                    para promover o novo vídeo do YouTube.
                    """,
            verbose=True,
            tools=human_tools
        )