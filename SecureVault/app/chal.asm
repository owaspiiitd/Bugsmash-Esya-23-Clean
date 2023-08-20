section .data
    secret_key  db 0x31, 0x32, 0x33, 0x34
    user_input  times 0x4 db 0x00

section .text
    global _start

_start:
    mov edx, 0xb
    mov ecx, instructions
    mov ebx, 0x1
    mov eax, 0x4
    int 0x80

    mov edx, 0x4
    mov ecx, user_input
    mov ebx, 0x0
    mov eax, 0x3
    int 0x80

    mov edi, user_input
    mov esi, secret_key
    xor eax, eax

.loop:
    mov al, byte [edi]
    cmp al, byte [esi]
    jnz .fail
    inc edi
    inc esi
    loop .loop

    mov edx, 0x9
    mov ecx, access_granted
    mov ebx, 0x1
    mov eax, 0x4
    int 0x80

    jmp .exit

.fail:
    mov edx, 0x7
    mov ecx, access_denied
    mov ebx, 0x1
    mov eax, 0x4
    int 0x80

.exit:
    mov eax, 0x1
    xor ebx, ebx
    int 0x80

section .data
    instructions db "Enter PIN: " 
    access_granted db "Correct!", 0xa
    access_denied db "Wrong!", 0xa
