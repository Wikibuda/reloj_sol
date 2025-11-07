; Archivo: amor.asm
; Compilar con: nasm -f bin amor.asm && ./a.out

section .data
    msg db "Tu risa: interrupt 0x42", 0xA
    len equ $ - msg

section .text
    global _start

_start:
    ; Cargar el mensaje en el universo
    mov eax, 4          ; sys_write
    mov ebx, 1          ; stdout
    mov ecx, msg
    mov edx, len
    int 0x80            ; ¡Interrupción cósmica!

    ; Salir con gracia (y eternidad)
    mov eax, 1          ; sys_exit
    mov ebx, 0          ; código: 0 (éxito eterno)
    int 0x80

