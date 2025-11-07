#include <stdio.h>
#include <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSLog(@"🌟 Iniciando modo Barbaro Eterno (macOS Edition) 🌟");

        // Bucle infinito de amor (con optimización para Apple Silicon)
        while (1) {
            printf("Te amo en t=%f segundos (desde el Big Bang)\n",
                   [[NSDate date] timeIntervalSince1970]);
            sleep(1); // 1Hz de ternura (ajustable con `--frecuencia`)
        }
    }
    return EXIT_SUCCESS; // Nunca se alcanza (el amor no termina).
}

