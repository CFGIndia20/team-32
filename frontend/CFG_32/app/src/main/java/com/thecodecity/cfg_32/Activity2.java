package com.thecodecity.cfg_32;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONException;
import org.json.JSONObject;
//import org.
import com.google.gson.Gson;
import com.hsalf.smilerating.SmileRating;
import java.io.IOException;
import java.util.StringTokenizer;
import java.lang.reflect.Array;
import java.util.ArrayList;
import org.json.JSONArray;
import org.w3c.dom.Text;

public class Activity2 extends AppCompatActivity {
    private TextView textViewQuestion;
    private TextView textViewQuestionCount;
    private Button buttonNext;
    private int questionCounter = 0;
    private int questionCountTotal;

    Gson g = new Gson();
    String Questions;
    JSONObject jsonObj;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        System.out.println("In the page ");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.page2);
        Intent intent=getIntent();
        Questions=intent.getStringExtra("Questions");
//        String[] l =Questions.split("{Question': '");
        TextView question=findViewById(R.id.textViewQuestion1);
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

        final TextView t1 = findViewById(R.id.text_view_count1);
        // TextView t2 = findViewById(R.id.textViewQuestion);
        //  t2.setText("How was the cleanliness ?");
        t1.setText("How satisfied are you with your stay? ");
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
        SmileRating smileRating = (SmileRating) findViewById(R.id.smile_rating1);
        smileRating.setOnSmileySelectionListener(new SmileRating.OnSmileySelectionListener() {
            @Override
            public void onSmileySelected(int smiley, boolean reselected) {
                switch (smiley) {
                    case SmileRating.BAD:
                        Toast.makeText(Activity2.this, "BAD", Toast.LENGTH_SHORT).show();
//                        rate=1;
                        break;
                    case SmileRating.GOOD:
                        Toast.makeText(Activity2.this, "GOOD", Toast.LENGTH_SHORT).show();

                        break;
                    case SmileRating.GREAT:
                        Toast.makeText(Activity2.this, "GREAT", Toast.LENGTH_SHORT).show();
                        break;
                    case SmileRating.OKAY:
                        Toast.makeText(Activity2.this, "OKAY", Toast.LENGTH_SHORT).show();
                        break;
                    case SmileRating.TERRIBLE:
                        Toast.makeText(Activity2.this, "TERRIBLE", Toast.LENGTH_SHORT).show();
                        break;
                }
            }

        });

        smileRating.setOnRatingSelectedListener(new SmileRating.OnRatingSelectedListener() {
            @Override
            public void onRatingSelected(int level, boolean reselected) {
                Toast.makeText(Activity2.this, "Selected Rating " + level, Toast.LENGTH_SHORT).show();
            }
        });
    }
    public void cl2(View view) {
        Intent intent2 = new Intent(Activity2.this, Final.class);
        startActivity(intent2);
    }

}
