from functools import partial
from crewai import Task
from textwrap import dedent


class YoutubeAutomationTasks():

    def manage_youtube_video_creation(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""
                            Supervisionar o processo de preparação do YouTube, incluindo pesquisa de mercado, criação de títulos, 
                            criação de descrição e criação de e-mails necessários para fazer um vídeo do YouTube. O objetivo final 
                            é gerar um relatório incluindo uma tabela de pesquisa, títulos potenciais com alta taxa de cliques, 
                            uma descrição para o vídeo do YouTube e uma atualização de newsletter por e-mail sobre o novo vídeo.
                               
                O tópico do vídeo é: {video_topic}
                As informações do vídeo são: {video_details}

            Exemplo de Saída:
                                   
            # Tabela de Pesquisa de Concorrência no YouTube: 
            - Vídeo 1:
                - Título: "Como Fazer um Vídeo para o YouTube"
                - Contagem de Visualizações: 100.000
                - Dias Desde a Publicação: 30
                - Contagem de Inscritos no Canal: 1.000
                - URL do Vídeo: https://www.youtube.com/watch?v=1234
            - Vídeo 2:
                - Título: "Como Fazer um Vídeo para o YouTube"
                - Contagem de Visualizações: 100.000
                - Dias Desde a Publicação: 30
                - Contagem de Inscritos no Canal: 1.000
                - URL do Vídeo: https://www.youtube.com/watch?v=1234

            [THE REST OF THE YOUTUBE COMPETITION RESEARCH GOES HERE]
                                   
            - Video 15:
                - Título: "Como Fazer um Vídeo para o YouTube"
                - Contagem de Visualizações: 100.000
                - Dias Desde a Publicação: 30
                - Contagem de Inscritos no Canal: 1.000
                - URL do Vídeo: https://www.youtube.com/watch?v=1234              
                                   
            # Títulos Potenciais de Alta Taxa de Cliques:
            - Como Fazer um Vídeo para o YouTube
            - Como Fazer um Vídeo para o YouTube em 2021
            - Como Fazer um Vídeo para o YouTube para Iniciantes
            [O RESTANTE DOS TÍTULOS POTENCIAIS DE ALTA TAXA DE CLIQUES VAI AQUI]
                                   
            # Descrição do Vídeo no YouTube:
            🤖 Baixe o Código-Fonte do CrewAI Aqui:
            https://brandonhancock.io/crewai-updated-tutorial-hierarchical 

            Não esqueça de Curtir e Inscrever-se se você é fã de código-fonte gratuito 😉

            Pronto para liderar uma revolução em IA? Assista e aprenda como construir seu próprio CrewAI do zero usando os recursos 
            mais recentes do CrewAI, e prepare-se para implantar um exército de agentes de IA sob seu comando. Este vídeo é seu guia 
            definitivo para criar uma força de trabalho digital poderosa, aprimorando seus projetos com automação inteligente e fluxos 
            de trabalho simplificados. Descubra os segredos para personalizar agentes de IA, colocá-los em tarefas e gerenciar uma 
            operação suave com o CrewAI. É hora de ampliar suas capacidades tecnológicas, e depois deste tutorial, você estará equipado 
            para engenhar uma equipe de IA que transforma qualquer desafio complexo em uma tarefa simples. Inicie sua jornada para a 
            maestria em IA com o CrewAI hoje!



            📰 Fique atualizado com meus últimos projetos e insights:
            LinkedIn: https://www.linkedin.com/in/brandon-hancock-ai/
       

            Resources:
            - https://github.com/joaomdmoura/crewAI-examples/
            - https://www.crewai.io/
            - https://twitter.com/joaomdmoura/status/1756428892045496608
            - https://serper.dev/
            
            # Anúncio por E-mail:
            
            Olá [NOME VAI AQUI]!

            Atualização empolgante: a nova versão do CrewAI está aqui, tornando-o mais rápido e confiável!

            Você amou nosso primeiro tutorial do CrewAI, então acabei de publicar um novo para você.

            Neste tutorial, você vai se atualizar com os novos recursos do CrewAI. Em seguida, aplicaremos essas atualizações construindo uma 
            Newsletter de IA, demonstrando como usar o que você aprendeu em um projeto real.

            [PRÉVIA DO VÍDEO AQUI]

            Here's what's in store:

            Aqui está o que te espera:

           - Aprenda a gerenciar uma equipe com o novo fluxo de trabalho Hierárquico do CrewAI.
           - Descubra como as tarefas assíncronas podem aumentar sua eficiência.
           - Descubra como o recurso de Saída Esperada garante precisão e confiabilidade.
           - Além disso, muitos outros insights!
           - Mergulhe no tutorial para explorar as funções aprimoradas do CrewAI:

            [PRÉVIA DO VÍDEO AQUI]

            Dúvidas ou quer compartilhar como você está indo? Me envie um e-mail ou comente no YouTube.

            Feliz programação!

            Nós vemos por ai.
            Anderson Vieira
            """),
            agent=agent,
            output_file="output/YouTube_Video_Creation_Report.txt",
            expected_output=dedent(f"""
                                   Gere um relatório formatado exatamente como o exemplo de relatório fornecido anteriormente.
                                   Certifique-se de que o relatório contenha 15 vídeos, 10 títulos potenciais de alta taxa de 
                                   cliques (CTRO), uma descrição de vídeo do YouTube e uma newsletter por e-mail. O vídeo pesquisado 
                                   deve conter todos os detalhes requeridos e URLs válidos.
                                   """)
        )

    def manage_youtube_video_research(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Para um determinado tópico e descrição de vídeo, procure vídeos no YouTube para encontrar 
                                   15 vídeos de alto desempenho sobre o mesmo tópico. Uma vez encontrados os vídeos, pesquise 
                                   os detalhes do vídeo do YouTube para completar os campos que faltam no CSV de pesquisa. 
                                   Ao delegar tarefas para outros agentes, certifique-se de incluir a URL do vídeo que você 
                                   precisa que eles pesquisem.
                            
                Este CSV de pesquisa será utilizado por outros agentes para ajudá-los a gerar títulos e outros aspectos do novo 
                 vídeo do YouTube que estamos planejando criar.
                               
                Esboço do CSV de pesquisa:
                - Título do vídeo
                - Contagem de visualizações
                - Dias desde a publicação
                - Contagem de inscritos no canal
                - URL do vídeo
                       
                O tópico do vídeo é: {video_topic}
                As informações do vídeo são: {video_details}

                Notas importantes: 
                - Certifique-se de que o CSV utilize ; como delimitador
                - Certifique-se de que o esboço final do CSV de pesquisa não contenha vídeos duplicados
                - É SUPER IMPORTANTE que você apenas preencha o CSV de pesquisa com vídeos reais do YouTube 
                    e URLs do YouTube que realmente levem ao vídeo do YouTube.
                """),
            agent=agent,
            expected_output=dedent(f"""
                Título do Vídeo; Contagem de Visualizações; Dias Desde a Publicação; Contagem de Inscritos no Canal; URL do Vídeo
                Como Fazer um Vídeo para o YouTube; 100,000; 30; 1,000; https://www.youtube.com/watch?v=1234;
                Como Conseguir Seus Primeiros 1000 Inscritos; 100,000; 30; 1,000;  https://www.youtube.com/watch?v=1234;
                       ...              
                """)
        )

    def create_youtube_video_title(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Crie 10 títulos potenciais para um determinado tópico e descrição de vídeo do YouTube. 
                                   Também é muito importante usar os vídeos pesquisados para ajudar a gerar os títulos. Os títulos devem ter 
                                    menos de 70 caracteres e devem ter uma alta taxa de cliques.
                               
                Video Topic: {video_topic}
                Video Details: {video_details}
                """),
            agent=agent,
            expected_output=dedent(f"""
                - Tutorial do CrewAI para Iniciantes: Aprenda Como Usar as Últimas Funcionalidades do CrewAI
                - Tutorial do CrewAI: Curso Intensivo Completo para Iniciantes
                - Como Conectar LLMs Locais ao CrewAI [Ollama, Llama2, Mistral]
                - Como Usar o CrewAI para Automatizar Seu Fluxo de Trabalho
                - Tutorial do CrewAI: Como Construir uma Força de Trabalho Digital
                ...                
                """),
        )

    def create_youtube_video_description(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Crie uma descrição para um determinado tópico e descrição de vídeo do YouTube.     
                Video Topic: {video_topic}
                Video Details: {video_details}
                """),
            agent=agent,
            expected_output=dedent(f"""
                🤖 Download the CrewAI Source Code Here:
                https://brandonhancock.io/crewai-updated-tutorial-hierarchical 
                                   
                Don't forget to Like and Subscribe if you're a fan of free source code 😉
                                   
                Want to join a community of AI developers? Join the AI Developer Accelerator Skook Community for FREE:
                https://www.skool.com/ai-developers-9308

                Ready to lead an AI revolution? Watch and learn how to build your own CrewAI from the ground up using the latest CrewAI features, and get set to deploy an army of AI agents at your command. This video is your ultimate guide to creating a powerful digital workforce, enhancing your projects with intelligent automation and streamlined workflows. Discover the secrets to customizing AI agents, setting them on tasks, and managing a smooth operation with CrewAI. It’s time to amplify your tech capabilities, and after this tutorial, you'll be equipped to engineer an AI crew that transforms any complex challenge into a simple task. Start your journey to AI mastery with CrewAI today!

                📰 Stay updated with my latest projects and insights:
                LinkedIn: https://www.linkedin.com/in/brandon-hancock-ai/
                Twitter: https://twitter.com/bhancock_ai

                Resources:
                [LEAVE BLANK]
                                   
                Timestamps: 
                [LEAVE BLANK]
            """),
        )

    def create_email_announcement_for_new_video(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Crie um e-mail para enviar a uma lista de e-mails para promover o novo vídeo do YouTube.
                                                              
                Video Topic: {video_topic}
                Video Details: {video_details}

                Here are a few previous email announcements that you can use as inspiration. 
                
                Important Notes:
                - Make sure to copy my style, tone, and voice when writing the email.
                -  Before submitting your final work, you MUST have a human review your tenative final email.

                Email 1:
                ----------------
                Subject: New CrewAI Tutorial: Learn How To Use the Latest CrewAI Features

                Hey [FIRST NAME GOES HERE]!

                Exciting update: CrewAI's new version is here, making it quicker and more dependable!

                You loved our first CrewAI tutorial, so I just published a new one for you.

                In this tutorial, you'll get up to speed with CrewAI's new features. We'll then apply these updates by building an AI Newsletter, demonstrating how to use what you've learned in a real project.

                video preview​
                Here's what's in store:

                Learn to manage a team with CrewAI's new Hierarchical workflow.
                Discover how asynchronous tasks can boost your efficiency.
                Find out how the Expected Output feature ensures accuracy and reliability.
                Plus, lots more insights!
                Dive into the tutorial to explore CrewAI's enhanced functions:

                video preview​
                Questions or want to share how you're doing? Email me or comment on YouTube.

                Happy coding!

                Cheers, 
                Brandon Hancock
                ----------------


                Email 2:
                ----------------
                Subject: New CrewAI + Ollama Tutorial: Learn How To Run CrewAI for Free

                Hey [FIRST NAME GOES HERE]!

                You asked, and I delivered! 🚀

                After posting my latest CrewAI tutorial, the 2 biggest questions flooding my inbox have been:

                How do I connect CrewAI with LLMs like Llama 2 and Mistral?
                How can I run CrewAI for free?
                Since it would be wrong to leave you hanging, I just published a new step-by-step YouTube tutorial for you to answer these questions!

                [VIDEO PREVIEW HERE]

                This tutorial shows you how to connect CrewAI with LLMs running on your own machine, which let's you run CrewAI completely for free!

                🎥 New Tutorial Alert: Connect CrewAI with Llama 2 & Mistral for Free!

                In this step-by-step guide for beginners, I'm pumped to walk you through the process of connecting CrewAI to locally running LLMs on your machine. Whether you're working with Llama 2, Mistral, or another LLM, I've got you covered. This tutorial is your golden ticket to running your crew at no cost!

                Here's a sneak peek of what you'll learn:

                Understanding CrewAI, Ollama, Llama 2, and Mistral: Dive into the basics of these powerful tools and their potential to revolutionize your projects.
                Step-by-Step Integration: Follow my detailed instructions to seamlessly connect CrewAI with Llama 2 or Mistral.
                Run Your Crew for Free: Yes, you read that right! I'll show you how to leverage these technologies without dipping into your wallet.
                I can't wait for you to check out the tutorial and start experimenting with CrewAI, Ollama, Llama 2, and Mistral. Your feedback and questions are what fuel this community, so don't hesitate to drop a comment on the video or shoot me an email with your thoughts and experiences.

                [VIDEO PREVIEW HERE]

                Once again, you can check out the latest video here:

                Happy coding, and here's to many more innovative projects ahead!

                Cheers,
                Brandon Hancock
                ----------------
                """),
            agent=agent,
            expected_output=dedent(f"""Um e-mail que contém um assunto e corpo formatados exatamente como o exemplo de e-mail fornecido 
                                   anteriormente a você.
                                    """),
        )