import express from 'express';
import cors from 'cors';
import OpenAI from 'openai';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const port = process.env.PORT || 5000;

const apiKey = process.env.OPENAI_API_KEY?.replace(/(\r\n|\n|\r)/gm, "").trim();

const openai = new OpenAI({
  apiKey: apiKey,
});

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello from SSAFY Chatbot Backend!');
});

app.post('/api/chat', async (req, res) => {
  try {
    const { message } = req.body;
    console.log('Received message:', message);

    // Dynamically build the content payload
    const contentPayload: any[] = [{ type: "text", text: message.text || "" }];
    if (message.image) {
      contentPayload.push({
        type: "image_url",
        image_url: {
          url: message.image,
        },
      });
    }

    const response = await openai.chat.completions.create({
      model: "gpt-4-vision-preview",
      messages: [
        {
          role: "user",
          content: contentPayload,
        },
      ],
      max_tokens: 300,
    });

    const aiResponse = response.choices[0].message.content || "No response from AI.";

    res.json({
      id: Date.now().toString(),
      text: aiResponse,
      sender: 'ai',
    });

  } catch (error) {
    if (error instanceof OpenAI.APIError) {
      console.error('OpenAI API Error:', error.status, error.name);
      console.error('Error Details:', error.message);
      res.status(error.status || 500).json({ error: `OpenAI API Error: ${error.message}` });
    } else {
      console.error('Non-OpenAI Error:', error);
      res.status(500).json({ error: 'An unexpected error occurred on the server.' });
    }
  }
});

app.listen(port, () => {
  console.log(`Server is running on port: ${port}`);
});
