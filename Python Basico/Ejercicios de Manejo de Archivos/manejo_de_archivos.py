def open_and_print_file_per_line(path):
    with open(path) as file:
        songs = file.readlines()

    songs = [line.strip() for line in songs]

    songs.sort()

    return songs

ordered_songs = open_and_print_file_per_line('canciones.txt')

with open("canciones_nuevo.txt", "w") as archivo:
    for song in ordered_songs:
        archivo.write(song + "\n")

print(f'Archivo creado con canciones ordenadas. {ordered_songs}')