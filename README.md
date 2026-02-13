# 🏺 Gemini Historical Artifact Description App

A Streamlit web application that leverages Google's Gemini 1.5 Flash AI to generate detailed, engaging descriptions of historical artifacts from uploaded images.

## 📋 Overview

The Gemini Historical Artifact Description App allows historians, museum curators, students, and history enthusiasts to upload images of historical artifacts and receive comprehensive AI-generated descriptions. The app provides customizable word counts and includes interesting historical facts to enhance the user experience.

## ✨ Features

- **🖼️ Image Upload**: Support for JPG, JPEG, and PNG image formats
- **🤖 AI-Powered Descriptions**: Utilizes Google's Gemini 1.5 Flash model for intelligent artifact analysis
- **📝 Customizable Output**: Specify desired word count for generated descriptions
- **💡 Historical Facts**: Displays random historical facts while processing to engage users
- **⚡ Real-time Processing**: Fast response times with Google's advanced AI model
- **🎨 User-Friendly Interface**: Clean, intuitive Streamlit interface

## 🚀 Demo Use Cases

### Scenario 1: Ancient Egyptian Artifact
A historian specializing in Ancient Egypt uploads an image of Tutankhamun's Golden Mask with a 1200-word count request. The app generates a detailed description covering the artifact's origin, historical significance, and cultural context.

### Scenario 2: Renaissance Art Analysis
A museum curator uploads Leonardo da Vinci's Notebook and specifies an 800-word count. The AI provides a comprehensive description filled with historical context and artistic significance.

### Scenario 3: Medieval Artifact Study
A student researching medieval history uploads an image of a medieval sword and requests detailed information for their research paper.

## 🛠️ Technology Stack

- **Python 3.x**: Core programming language
- **Streamlit**: Web application framework
- **Google Gemini 1.5 Flash API**: AI model for description generation
- **PIL (Pillow)**: Image processing library
- **python-dotenv**: Environment variable management

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get it here](https://ai.google.dev/))

### Step 1: Clone the Repository

```bash
git clone https://github.com/Sujeth12/gemini-artifact-app.git
cd gemini-artifact-app
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Alternatively, you can configure the API key directly in the Streamlit app interface.

## 🎯 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the App

1. **Enter Your API Key**: Input your Google Gemini API key in the sidebar
2. **Upload an Image**: Click on the file uploader and select an image of a historical artifact (JPG, JPEG, or PNG)
3. **Enter a Prompt**: Describe what information you want about the artifact
4. **Specify Word Count**: Enter your desired description length
5. **Generate Description**: Click the "🔍 Generate Artifact Description" button
6. **View Results**: The AI-generated description will appear below, along with your uploaded image

### Example Prompt

```
You are a historian. Please describe the historical artifact in the image and provide detailed information, including its name, origin, historical period, cultural significance, and any interesting facts about it.
```

## 📁 Project Structure

```
gemini-artifact-app/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── .env                  # Environment variables (not in repo)
└── README.md             # Project documentation
```

## 🔑 Key Functions

### `input_image_setup(uploaded_file)`
Processes the uploaded image file and converts it to the format required by the Gemini API.

**Parameters:**
- `uploaded_file`: The image file uploaded through Streamlit's file uploader

**Returns:**
- List containing image data in the format required by Gemini API

### `get_gemini_response(input_text, image_data, input_prompt)`
Sends the image and prompt to Google's Gemini 1.5 Flash model and retrieves the generated description.

**Parameters:**
- `input_text`: User's custom prompt or question
- `image_data`: Processed image data
- `input_prompt`: System-level instruction for the AI model

**Returns:**
- Generated text description from the AI model

## 📝 Requirements

```
streamlit
google-generativeai
python-dotenv
Pillow
```

## 🔒 Security Considerations

- **API Key Protection**: Never commit your `.env` file or expose your API key in public repositories
- **Image Validation**: The app validates file types before processing
- **Error Handling**: Comprehensive error handling for API failures and invalid inputs

## 🎨 Customization

### Modifying the AI Prompt

You can customize the system prompt in `app.py` to change how the AI analyzes artifacts:

```python
input_prompt = """
Your custom instructions here...
Specify the tone, detail level, and focus areas for descriptions.
"""
```

### Adjusting Word Count Limits

Modify the word count input validation to set different minimum or maximum values:

```python
word_count = st.number_input(
    "Word Count", 
    min_value=100, 
    max_value=5000,  # Adjust as needed
    value=500
)
```

## 🐛 Troubleshooting

### Common Issues

**Issue: "Invalid API Key"**
- Solution: Verify your Google Gemini API key is correct and active

**Issue: "Image Upload Failed"**
- Solution: Ensure the image is in JPG, JPEG, or PNG format and under 10MB

**Issue: "Module Not Found"**
- Solution: Run `pip install -r requirements.txt` to install all dependencies

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Sujeth12**
- GitHub: [@Sujeth12](https://github.com/Sujeth12)

## 🙏 Acknowledgments

- Google for providing the Gemini AI API
- Streamlit for the excellent web framework
- The open-source community for inspiration and support

## 📧 Contact

For questions, suggestions, or feedback, please open an issue on GitHub or contact the repository owner.

## 🔮 Future Enhancements

- [ ] Multi-language support for descriptions
- [ ] Batch processing for multiple artifacts
- [ ] Export descriptions to PDF/Word
- [ ] Historical timeline visualization
- [ ] Artifact comparison feature
- [ ] Integration with museum databases
- [ ] Audio narration of descriptions
- [ ] User authentication and history tracking

## 📊 Version History

- **v1.0.0** (Current)
  - Initial release
  - Basic artifact description generation
  - Image upload functionality
  - Customizable word count
  - Historical facts feature

---

**Note**: This application uses Google's Gemini AI, which requires an active internet connection and valid API key. Usage is subject to Google's terms of service and API rate limits.

Made with ❤️ for history enthusiasts and researchers worldwide
