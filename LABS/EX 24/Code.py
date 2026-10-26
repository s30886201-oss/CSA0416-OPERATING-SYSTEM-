#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main()
{
    int fd;
    char buffer[100];
    char text[] = "Welcome to UNIX File Management";

    /* Create and open a file */
    fd = open("sample.txt", O_CREAT | O_RDWR | O_TRUNC, 0644);

    if (fd < 0)
    {
        perror("File opening failed");
        return 1;
    }
    printf("File created and opened successfully.\n");

    /* Write data into file */
    write(fd, text, strlen(text));
    printf("Data written successfully.\n");

    /* Move file pointer to beginning */
    lseek(fd, 0, SEEK_SET);

    /* Read data from file */
    int n = read(fd, buffer, sizeof(buffer) - 1);

    if (n < 0)
    {
        perror("File reading failed");
        close(fd);
        return 1;
    }

    buffer[n] = '\0';
    printf("Data read from file: %s\n", buffer);

    /* Close the file */
    close(fd);
    printf("File closed successfully.\n");

    /* Delete the file */
    if (unlink("sample.txt") == 0)
        printf("File deleted successfully.\n");
    else
        perror("File deletion failed");

    return 0;
}
