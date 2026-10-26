#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <dirent.h>
#include <string.h>

int main()
{
    int fd;
    char buffer[100];
    struct stat info;
    DIR *dir;
    struct dirent *entry;

    /* Create and open a file */
    fd = open("sample.txt", O_CREAT | O_RDWR | O_TRUNC, 0644);

    if (fd == -1)
    {
        perror("open");
        return 1;
    }

    printf("File opened successfully.\n");

    /* Write data into file */
    write(fd, "Hello UNIX System Calls", 23);

    /* fcntl system call */
    int flags = fcntl(fd, F_GETFL);
    printf("File status flags: %d\n", flags);

    /* lseek system call */
    lseek(fd, 0, SEEK_SET);
    int n = read(fd, buffer, sizeof(buffer) - 1);

    if (n < 0)
    {
        perror("read");
        close(fd);
        return 1;
    }

    buffer[n] = '\0';
    printf("File contents: %s\n", buffer);

    /* stat system call */
    if (stat("sample.txt", &info) == 0)
    {
        printf("File size: %lld bytes\n",
               (long long)info.st_size);
        printf("File permissions: %o\n",
               (unsigned int)(info.st_mode & 0777));
    }
    else
    {
        perror("stat");
    }

    close(fd);

    /* opendir and readdir */
    dir = opendir(".");

    if (dir == NULL)
    {
        perror("opendir");
        return 1;
    }

    printf("\nFiles in current directory:\n");

    while ((entry = readdir(dir)) != NULL)
    {
        printf("%s\n", entry->d_name);
    }

    closedir(dir);

    return 0;
}
