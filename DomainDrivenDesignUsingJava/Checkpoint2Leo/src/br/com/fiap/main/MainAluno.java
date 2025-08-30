package br.com.fiap.main;
import br.com.fiap.bean.Aluno;
import javax.swing.*;
import java.time.LocalDate;

// RM: 565465 - Nome: Marcelo Alexandre dos Santos
// RM: 565321 - Poliana Batista Sarmento
// RM: 552417 - Leonardo Rodrigues Martins
// RM: 564538 - Aline Lourenço Carvalho

public class MainAluno {
    public static void main(String[] args) {

        // Criando os Objetos da Classe Aluno

        Aluno aluno1 = new Aluno();
        Aluno aluno2 = new Aluno();
        Aluno aluno3 = new Aluno(89630, "Leonardo", 2004);
        Aluno aluno4 = new Aluno(595485, "Poliana", 2003);

        // Atribuindo valores a todos os objetos
        aluno1.setNomeCompleto("Aline Lourenço Carvalho");
        aluno1.setRegistroMatricula(564538);
        aluno1.setAnoNascimento(1998);

        aluno2.setNomeCompleto("Leonardo Rodrigues Martins");
        aluno2.setRegistroMatricula(552417);
        aluno2.setAnoNascimento(2003);

        // String auxiliar do JOptionPane
        String auxiliar;

        // Declarando a Classe LocalDate para armazenar o ano atual
        LocalDate dataAtual = LocalDate.now();
        int anoAtual = dataAtual.getYear();

        try {
            // Aluno 1

            auxiliar = JOptionPane.showInputDialog("Turma "+dataAtual.getYear()+"\n\nAluno 1\n\nDigite seu registro de matrícula:");
            aluno1.setRegistroMatricula(Integer.parseInt(auxiliar));
            auxiliar = JOptionPane.showInputDialog("Turma "+dataAtual.getYear()+"\n\nAluno 1\n\nDigite o seu nome completo:");
            aluno1.setNomeCompleto(auxiliar);
            auxiliar = JOptionPane.showInputDialog("Turma "+dataAtual.getYear()+"\n\nAluno 1\n\nDigite seu ano de nascimento");
            aluno1.setAnoNascimento(Integer.parseInt(auxiliar));

            // Aluno 2

            auxiliar = JOptionPane.showInputDialog("Turma "+dataAtual.getYear()+"\n\nAluno 2\n\nDigite seu registro de matrícula:");
            aluno2.setRegistroMatricula(Integer.parseInt(auxiliar));
            auxiliar = JOptionPane.showInputDialog("Turma "+dataAtual.getYear()+"\n\nAluno 2\n\nDigite o seu nome completo:");
            aluno2.setNomeCompleto(auxiliar);
            auxiliar = JOptionPane.showInputDialog("Turma "+dataAtual.getYear()+"\n\nAluno 2\n\nDigite seu ano de nascimento");
            aluno2.setAnoNascimento(Integer.parseInt(auxiliar));

            // Formatando Mensagens

            String mensagem1 = String.format("Matrícula %d\n\n Aluno 1\n\nRm: %d\nNome completo: %s\nIdade: %d anos\n\n",dataAtual.getYear(),aluno1.getRegistroMatricula(),aluno1.getNomeCompleto(),aluno1.calcularIdade(dataAtual));

            String mensagem2 = String.format("Matrícula %d\n\n Aluno 2\n\nRm: %d\nNome completo: %s\nIdade: %d anos\n\n",dataAtual.getYear(),aluno2.getRegistroMatricula(),aluno2.getNomeCompleto(),aluno2.calcularIdade(dataAtual));

            String mensagem3 = String.format("Matrícula %d\n\n Aluno 3\n\nRm: %d\nNome completo: %s\nIdade: %d anos\n\n",dataAtual.getYear(),aluno3.getRegistroMatricula(),aluno3.getNomeCompleto(),aluno3.calcularIdade(dataAtual));

            String mensagem4 = String.format("Matrícula %d\n\n Aluno 4\n\nRm: %d\nNome completo: %s\nIdade: %d anos\n\n",dataAtual.getYear(),aluno4.getRegistroMatricula(),aluno4.getNomeCompleto(),aluno4.calcularIdade(dataAtual));

            // Exibindo Mensagens

            JOptionPane.showMessageDialog(null, mensagem1);
            JOptionPane.showMessageDialog(null, mensagem2);
            JOptionPane.showMessageDialog(null, mensagem3);
            JOptionPane.showMessageDialog(null, mensagem4);

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "RM ou Ano de Nascimento inválido! Digite novamente");
        }
    }
}
