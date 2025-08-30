package br.com.fiap.main;

import br.com.fiap.bean.RadioPDF4;
import br.com.fiap.bean.TelevisorPDF4;

import java.util.Scanner;

public class MainRadio {
    public static void main(String[] args) {
        RadioPDF4 radio1 = new RadioPDF4();

        radio1.estacao = 89.1f;
        radio1.volume = 5;

        radio1.trocarEstacao(92.5f);
        radio1.aumentarVolume();
        radio1.aumentarVolume();

        System.out.println("Volume atual: "+radio1.volume+"\nEstação atual: "+radio1.estacao);
    }
}
