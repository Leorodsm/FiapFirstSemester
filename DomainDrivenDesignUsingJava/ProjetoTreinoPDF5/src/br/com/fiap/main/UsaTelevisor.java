package br.com.fiap.main;

import br.com.fiap.bean.Televisor;

public class UsaTelevisor {
    public static void main(String[] args) {
        Televisor televisor = new Televisor();

        televisor.canal = 5;
        televisor.volume = 7;
        televisor.trocarCanal(4);
        televisor.diminuirVolume();
        televisor.diminuirVolume();

        System.out.printf("Volume atual: %d\nCanal atual: %d",televisor.volume, televisor.canal);
    }
}
