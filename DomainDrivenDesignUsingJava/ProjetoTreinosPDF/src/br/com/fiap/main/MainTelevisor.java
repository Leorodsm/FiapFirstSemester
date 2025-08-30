package br.com.fiap.main;

import br.com.fiap.bean.TelevisorPDF4;

public class MainTelevisor {
    public static void main(String[] args) {
        TelevisorPDF4 televisor = new TelevisorPDF4();

        televisor.volume = 5;
        televisor.canal = 4;

        televisor.diminuirVolume();
        televisor.trocarCanal(2);

        System.out.println("Volume: "+televisor.volume+"\nCanal: "+televisor.canal);
    }
}
