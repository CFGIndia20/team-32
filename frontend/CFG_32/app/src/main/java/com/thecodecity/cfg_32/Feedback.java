package com.thecodecity.cfg_32;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONObject;
//import org.
import com.google.gson.Gson;
import com.hsalf.smilerating.SmileRating;

import org.json.JSONArray;

public class Feedback extends AppCompatActivity {
    private TextView textViewQuestion;
    private TextView textViewQuestionCount;
    private Button buttonNext;
    private int questionCounter=0;
    private int questionCountTotal;
    Gson g=new Gson();
    String Questions;
    JSONObject jsonObj;
  //  TextView t1 = findViewById(R.id.text_view_count);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        System.out.println("feedback class starts");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_feedback);
        Intent intent=getIntent();
        Questions=intent.getStringExtra("Questions");
//        String[] l =Questions.split("{Question': '");
        TextView question=findViewById(R.id.textViewQuestion);
/*
        try{
            jsonObj=new JSONObject(Questions);
            JSONArray questions = jsonObj.getJSONArray("Questions");
            System.out.println("Qns: "+questions);
            for (int i =0;i<questions.length();i++){
                JSONObject j=questions.getJSONObject(i);
                System.out.println("hi hello"+j.getString("Question"));
                question.setText(j.getString("Question"));

            }
        }
        catch (Exception e){
            e.printStackTrace();
        }
*/
//        StringTokenizer st=new StringTokenizer(Questions,"[{':,}]");

       final TextView t1 = findViewById(R.id.text_view_count);
       // TextView t2 = findViewById(R.id.textViewQuestion);
      //  t2.setText("How was the cleanliness ?");
      t1.setText("How was the cleanliness ?");
//            try {
//                 jsonObj = new JSONObject(Questions);
//                System.out.println("JSONNNN "+ jsonObj);
//
//            } catch (JSONException e) {
//                e.printStackTrace();
//            }
//System.out.println("JSONNNN "+ jsonObj);

//        JSONObject json=(JSONObject)
       // String t2= "{‘'Questions’: [{'Question': 'How was cleanliness?',’LangQuestionText’:’[Other language]’,’LangQuestionAudio’:’[gTTs obj]’, 'id': '1'}, {'Question': 'how was the food qualty?',’LangQuestionText’:’[Other language]’,’LangQuestionAudio’:’[gTTs obj]’, 'id': '2'}, {'Question': 'how clean was water provided?' ,’LangQuestionText’:’[Other language]’,’LangQuestionAudio’:’[gTTs obj]’ , 'id': '3'}, {'Question': 'how was the neighbourhood?' ,’LangQuestionText’:’[Other language]’,’LangQuestionAudio’:’[gTTs obj]’, 'id': '4'}] }";
//    System.out.println("St value:"+st.nextToken());
        String q="";
        String word,word1;
        int flag=0;/*
        while (st.hasMoreTokens()){
            word=st.nextToken();
            if (word.equals("Question") || flag!=0){
                word1=st.nextToken();
                q+=word1.concat(" ");
                flag =1;
                if (st.nextToken().equals("’LangQuestionText’")){
                    flag=0;
                }

            }
        }*/
        question.setText(q);

//        textViewQuestionCount = findViewById(R.id.text_view_count);
//        buttonNext = findViewById(R.id.button_next);
//        public int rate;
        SmileRating smileRating = (SmileRating) findViewById(R.id.smile_rating);
        smileRating.setOnSmileySelectionListener(new SmileRating.OnSmileySelectionListener() {
            @Override
            public void onSmileySelected(int smiley, boolean reselected) {
                switch (smiley) {
                    case SmileRating.BAD:
                        Toast.makeText(Feedback.this, "BAD", Toast.LENGTH_SHORT).show();
//                        rate=1;
                        break;
                    case SmileRating.GOOD:
                        Toast.makeText(Feedback.this, "GOOD", Toast.LENGTH_SHORT).show();

                        break;
                    case SmileRating.GREAT:
                        Toast.makeText(Feedback.this, "GREAT", Toast.LENGTH_SHORT).show();
                        break;
                    case SmileRating.OKAY:
                        Toast.makeText(Feedback.this, "OKAY", Toast.LENGTH_SHORT).show();
                        break;
                    case SmileRating.TERRIBLE:
                        Toast.makeText(Feedback.this, "TERRIBLE", Toast.LENGTH_SHORT).show();
                        break;
                }
            }

        });

        smileRating.setOnRatingSelectedListener(new SmileRating.OnRatingSelectedListener() {
            @Override
            public void onRatingSelected(int level, boolean reselected) {
                Toast.makeText(Feedback.this, "Selected Rating " + level, Toast.LENGTH_SHORT).show();
            }
        });

}

    public void clmeth(View view) {
        Intent intent1 = new Intent(Feedback.this, Activity2.class);
        intent1.putExtra("Questions",Questions);
        startActivity(intent1);
    }
}
