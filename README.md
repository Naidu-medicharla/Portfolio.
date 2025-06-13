# Veera Venkata Naidu Medicharla - Portfolio Website

A modern, responsive portfolio website built with Flask, showcasing skills, projects, and achievements of Veera Venkata Naidu Medicharla, an ECE student and aspiring Data Analyst.

## Features

- 🎨 Modern, clean design with light theme
- 📱 Fully responsive (mobile-first approach)
- ✨ Smooth animations and transitions
- ⌨️ Typewriter effect in hero section
- 📧 Contact form with email integration
- 🎯 Interactive project showcase
- 🎮 Easter egg feature
- 📊 Skills visualization
- 🔍 SEO friendly

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Animations**: AOS.js
- **Icons**: Font Awesome
- **Fonts**: Poppins, Inter
- **Email**: Flask-Mail with Gmail SMTP

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd portfolio-website
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your email credentials:

   ```
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   SECRET_KEY=your-secret-key
   ```

5. Run the development server:

   ```bash
   python app.py
   ```

6. Visit `http://localhost:5000` in your browser

## Project Structure

```
portfolio-website/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css  # Main stylesheet
│   ├── js/
│   │   └── main.js    # JavaScript functionality
│   └── images/        # Project images
├── templates/
│   └── index.html     # Main template
└── README.md
```

## Customization

1. **Profile Information**: Edit the content in `templates/index.html`
2. **Styling**: Modify `static/css/style.css`
3. **Animations**: Adjust settings in `static/js/main.js`
4. **Projects**: Update project cards in the HTML
5. **Skills**: Modify the skills grid in the HTML

## Deployment

1. Choose a hosting platform (e.g., Heroku, PythonAnywhere)
2. Set up environment variables
3. Configure Gmail SMTP settings
4. Deploy using platform-specific instructions

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Veera Venkata Naidu Medicharla

- Email: [your-email@example.com]
- LinkedIn: [your-linkedin]
- GitHub: [your-github]
