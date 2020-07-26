package com.thecodecity.cfg_32;

import android.os.Bundle;
import android.content.Intent;

import androidx.appcompat.app.AppCompatActivity;

import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import java.util.StringTokenizer;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {
    private TextView mTextViewResult;

    EditText phonenum;
 public   String myResponse;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
//        RelativeLayout rlayout = findViewById(R.id.)

//        Toolbar toolbar = findViewById(R.id.toolbar);
//        setSupportActionBar(toolbar);
//        mTextViewResult = findViewById(R.id.text_view_result);


    }

    public void clickMethod(View view) {
        Toast.makeText(this, "I am in the next page", Toast.LENGTH_SHORT).show();
        phonenum=(EditText) findViewById(R.id.phone_num);
        System.out.println("Test0: "+ (R.id.phone_num));
        String ph = phonenum.getText().toString();

        OkHttpClient client = new OkHttpClient();
//        String url = "https://1080838c0aba.ngrok.io/Question/"+phonenum.getText();
        String url="https://751e9a5b1eca.ngrok.io/Question/";
        url=url.concat(ph);
        System.out.println("Test1: "+ ph);

        //  Log.d("message", url);
        Request request = new Request.Builder()
                .url(url)
                .build();
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
             //   if (response.isSuccessful()) {
                  //  myResponse = response.body().string();

            myResponse="How was the cleanliness ? ";
                 //   myResponse=" {‘Questions’:[{'Question': 'How was cleanliness?',’LangQuestionText’:’[Other language]’,’LangQuestionAudio’:’[gTTs obj]’, 'id': '1'}, {'Question': 'how was the food qualty?',’LangQuestionText’:’[Other language]’,’LangQuestionAudio’:’[gTTs obj]’, 'id': '2'}, {'Question': 'how clean was water provided?' ,’LangQuestionText’:’[Other language]’,’LangQuestionAudio’:’[gTTs obj]’ , 'id': '3'}, {'Question': 'how was the neighbourhood?' ,’LangQuestionText’:’[Other language]’,’LangQuestionAudio’:’[gTTs obj]’, 'id': '4'}]}";
                //    Intent intent = new Intent(getApplicationContext(), Feedback.class);
                    Intent intent = new Intent(MainActivity.this, Feedback.class);
                    System.out.println("Response"+ myResponse);

                    intent.putExtra("Questions",myResponse);

                    startActivity(intent);
//                    MainActivity.this.runOnUiThread(new Runnable() {
//                        @Override
//                        public void run() {
//                            mTextViewResult.setText(myResponse);
//                        }
//                    });

                }
           // }

        });
       // Intent intent = new Intent(MainActivity.this, Feedback.class);

        System.out.println("Response22"+ myResponse);

    }
}
