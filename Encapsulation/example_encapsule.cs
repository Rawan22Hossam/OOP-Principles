public class Player
{
    private int score; // hidden from outside

    public int GetScore()
    {
        return score;
    }

    public void SetScore(int value)
    {
        if (value >= 0) // control access
            score = value;
    }
}