import React, { useState } from "react";
import { Link } from "react-scroll"; // Import for smooth scrolling
import "./App.css";

function App() {
  // State to handle form input
  const [formData, setFormData] = useState({
    title: "",
    location: "",
    date: "",
    testimony: "",
    email: "",
    message: "",
  });

  const [isRegister, setIsRegister] = useState(false); // Toggle Login/Register

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert("Your testimony has been submitted!"); // Placeholder for backend logic
    setFormData({ title: "", location: "", date: "", testimony: "", email: "", message: "" }); // Reset form
  };

  return (
    <div className="app">
      {/* Navigation Bar */}
      <nav className="navbar">
        <h1 className="logo">Ontario, Canada</h1>
        <ul className="nav-links">
          <li><Link to="home" smooth={true} duration={500}>Home</Link></li>
          <li><Link to="submit" smooth={true} duration={500}>Submit Evidence</Link></li>
          <li><Link to="about" smooth={true} duration={500}>About Us</Link></li>
          <li><Link to="contact" smooth={true} duration={500}>Contact Us</Link></li>
          <li><Link to="auth" smooth={true} duration={500}>{isRegister ? "Register" : "Login"}</Link></li>
        </ul>
      </nav>

      {/* Hero Section */}
      <header id="home" className="hero">
        <h1>Indigenous Communities Water Support Centre</h1>
        <p>Report water issues, track government promises, and fight for clean water.</p>
        <Link to="submit" smooth={true} duration={500}>
          <button className="cta-button">Submit Evidence</button>
        </Link>
      </header>

      {/* Submit Evidence Section */}
      <section id="submit" className="section">
        <div className="content">
          <h2>Submit Evidence</h2>
          <p>Help us collect and track evidence on water issues affecting Indigenous communities.</p>

          {/* Submission Form */}
          <form className="evidence-form" onSubmit={handleSubmit}>
            <label>Title of Testimony</label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleChange}
              placeholder="e.g., Water Outages in Our Community"
              required
            />

            <label>Location</label>
            <select name="location" value={formData.location} onChange={handleChange} required>
              <option value="">Select Community</option>
              <option value="First Nations">First Nations</option>
              <option value="Inuit">Inuit</option>
              <option value="Métis">Métis</option>
              <option value="Other">Other (Specify Below)</option>
            </select>
            {formData.location === "Other" && (
              <input
                type="text"
                name="location"
                placeholder="Enter your location"
                value={formData.location}
                onChange={handleChange}
                required
              />
            )}

            <label>Date of Incident</label>
            <input
              type="date"
              name="date"
              value={formData.date}
              onChange={handleChange}
              required
            />

            <label>Write Your Testimony</label>
            <textarea
              name="testimony"
              value={formData.testimony}
              onChange={handleChange}
              placeholder="Describe the issue in detail..."
              rows="5"
              required
            ></textarea>

            <button type="submit" className="submit-button">Check Current Records</button>
          </form>

          {/* Submit a Claim Button (Scrolls to Contact Us) */}
          <Link to="contact" smooth={true} duration={500}>
            <button className="claim-button">Submit a Claim</button>
          </Link>
        </div>
      </section>

      {/* Authentication Section (Login/Register) */}
      <section id="auth" className="section">
        <div className="auth-container">
          <h2>{isRegister ? "Register" : "Login"}</h2>

          <form className="auth-form">
            {isRegister && (
              <input type="text" placeholder="Full Name" />
            )}
            <input type="email" placeholder="Email Address" required />
            <input type="password" placeholder="Password" required />
            {isRegister && (
              <>
                <input type="password" placeholder="Confirm Password" required />
                <input type="text" placeholder="Community (Optional)" />
              </>
            )}

            <button type="submit">{isRegister ? "Register" : "Login"}</button>
          </form>

          <p className="toggle-text">
            {isRegister ? "Already have an account?" : "Don't have an account?"}{" "}
            <span onClick={() => setIsRegister(!isRegister)}>
              {isRegister ? "Login" : "Register"}
            </span>
          </p>
        </div>
      </section>

      {/* About Us Section */}
      <section id="about" className="section">
        <div className="content">
          <h2>About Us</h2>
          <p>We are dedicated to ensuring clean drinking water for Indigenous communities through accountability and action.</p>
        </div>
      </section>

      {/* Contact Us Section */}
      <section id="contact" className="section">
        <div className="content">
          <h2>Contact Us</h2>
          <p>We value your voice. Whether you need support, want to escalate your concern, or are looking for ways to get involved, we are here to help.</p>
          <br></br>
          <form className="evidence-form" onSubmit={handleSubmit}>
            <label>Email Address</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Enter your email"
              required
            />

            <label>Please describe your issue or inquiry in detail.</label>
            <textarea
              name="message"
              value={formData.message}
              onChange={handleChange}
              placeholder="Please describe your issue or inquiry in detail"
              rows="5"
              required
            ></textarea>

            <button type="submit" className="submit-button">Submit</button>
          </form>

          {/* Claim Button */}
          <a
            href="https://firstnationsdrinkingwater.ca/"
            target="_blank"
            rel="noopener noreferrer"
            className="claim-button"
          >
            Submit a Claim to the Government
          </a>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
        <p>© 2025 Ripple.AI | All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
