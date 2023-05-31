from pytube import YouTube


def progress_func(stream, chunk, bytes_remaining):
    print(".")
    
def complete_func(stream, file_handle):
    print("Baixado com sucesso!")


url = input("Digite a URL: ")
yt = YouTube(url,on_progress_callback=progress_func,
        on_complete_callback=complete_func)


highest_resolution_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
my_itag = highest_resolution_stream.itag
title = yt.title
stream = yt.streams.get_by_itag(my_itag)

print(f'Baixando: {title}')
# por padrão baixa no mesmo diretorio onde o arquivo python estiver
stream.download()

# idéias pra proxima atualização: interface gráfica, baixar somente áudio

