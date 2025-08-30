package br.com.fiap.bean;
import java.time.LocalDate;

// RM: 565465 - Marcelo Alexandre dos Santos
// RM: 565321 - Poliana Batista Sarmento
// RM: 552417 - Leonardo Rodrigues Martins
// RM: 564538 - Aline Lourenço Carvalho

public class Aluno {
    private int registroMatricula;
    private String nomeCompleto;
    private int anoDeNascimento;

    // Construtores ____________________________________________________

    /* Construtor Sem Parâmetros */
    public Aluno() {

    }

    /* Construtor Com Parâmetros */
    public Aluno(int registroMatricula, String nomeCompleto, int anoDeNascimento){
        this.registroMatricula = registroMatricula;
        this.nomeCompleto = nomeCompleto;
        this.anoDeNascimento = anoDeNascimento;
    }

    // Métodos Getters/Setters ____________________________________________________

    public int getRegistroMatricula() {
        return registroMatricula;
    }

    public void setRegistroMatricula(int registroMatricula) {
        try {
            if (registroMatricula >= 80000 && registroMatricula <= 599999) {
                this.registroMatricula = registroMatricula;
            } else {
                throw new Exception("Somente valores entre entre 80.000 e 599.999 são aceitos");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public String getNomeCompleto() {
        return nomeCompleto;
    }

    public void setNomeCompleto(String nomeCompleto) {
        this.nomeCompleto = nomeCompleto;
    }

    public int getAnoNascimento() {
        return anoDeNascimento;
    }

    public void setAnoNascimento(int anoDeNascimento) {
        LocalDate dataAtual = LocalDate.now();

        try {
            if (anoDeNascimento >= 1945 && anoDeNascimento <= dataAtual.getYear()) {
                this.anoDeNascimento = anoDeNascimento;
            } else {
                this.anoDeNascimento = 0;
                throw new Exception(" Só anos entre (1945 - "+dataAtual.getYear()+") são aceitos.");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    // Métodos da Classe ____________________________________________________

    public int calcularIdade(LocalDate dataAtual) {
        int idadeAluno;
        idadeAluno = dataAtual.getYear() - getAnoNascimento();

        return idadeAluno;
    }
}
