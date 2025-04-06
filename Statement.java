public class Statement{
    
    public String term;
    public double score;
    public String statement;

    public Statement(String term, double score, String statement){
        this.term = term;
        this.score = score;
        this.statement = statement;
    }

    public String getTerm(){
        return term;
    }

    public double getScore(){
        return score;
    }

    public String getStatement(){
        return statement;
    }

    @Override
    public String toString(){
        return term + score + statement;
    }

}
