package com.example.jobbuddy;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class MainActivity extends AppCompatActivity {

    private EditText email;
    private EditText password;

    private TextView signup;
    private TextView skip;

    private Button loginbtn;
    private Button gLogin;
    private Button fLogin;

    private FirebaseAuth mAuth;

    private ProgressDialog mDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mAuth = FirebaseAuth.getInstance();

//        if(mAuth.getCurrentUser() != null) {
//
//            startActivity(new Intent(getApplicationContext(), HomeActivity.class));
//            finish();
//
//        }

        mDialog = new ProgressDialog(this);

        email  = findViewById(R.id.email_login);
        password = findViewById(R.id.password_login);

        signup = findViewById(R.id.signup_txt);
        skip = findViewById(R.id.skip_txt);

        loginbtn = findViewById(R.id.login_btn);
        gLogin = findViewById(R.id.google_login_btn);
        fLogin = findViewById(R.id.fb_login_btn);

        signup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(), RegistrationActivity.class));
                finish();
            }
        });

        loginbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String emailId = email.getText().toString().trim();
                String mPass = password.getText().toString().trim();

                if(TextUtils.isEmpty(emailId))
                {
                    email.setError("Required Field");
                    return;
                }

                if(TextUtils.isEmpty((mPass))) {

                    password.setError("Required Field");
                    return;

                }

                mDialog.setMessage("Processing....");
                mDialog.show();

                mAuth.signInWithEmailAndPassword(emailId, mPass).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {

                        if(task.isSuccessful()) {

                            Toast.makeText(getApplicationContext(), "Login Successful", Toast.LENGTH_SHORT).show();
                            startActivity(new Intent(getApplicationContext(), HomeActivity.class));
                            mDialog.dismiss();
                            finish();

                        } else {

                            Toast.makeText(getApplicationContext(), "Something went Wrong!! Try again", Toast.LENGTH_LONG).show();
                            mDialog.dismiss();

                        }

                    }
                });

            }
        });

    }
}
