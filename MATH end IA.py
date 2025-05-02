import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt
import os

# 🎨 Configuration
st.set_page_config(page_title="Quiz Mathématiques - Limites", page_icon="🧠", layout="centered")
st.title("🧠 Quiz Mathématiques : Les Limites")
st.write("Bienvenue ! Testez vos connaissances sur les limites des fonctions.")

# 📚 Questions
questions = [
    r"\lim_{x \to 3} (2x + 1)",
    r"\lim_{x \to 0} x^2",
    r"\lim_{x \to 0} \frac{\sin(x)}{x}",
    r"\lim_{x \to \infty} \frac{1}{x}",
    r"\lim_{x \to 1} \frac{x^2 - 1}{x - 1}",
    r"\lim_{x \to 0} e^x",
    r"\lim_{x \to 2} (3x^2 + 2x - 5)",
    r"\lim_{x \to 0} \sqrt{x}",
    r"\lim_{x \to 2} \frac{x-2}{x^2-4}",
    r"\lim_{x \to 1} \ln(x)",
    r"\lim_{x \to 0} \cos(x)",
    r"\lim_{x \to 2} \frac{x+3}{x-2}",
    r"\lim_{x \to 2} \frac{x^2 - 4}{x - 2}",
    r"\lim_{x \to 0} \tan(x)",
    r"\lim_{x \to 1} \frac{x-1}{x^2-1}",
    r"\lim_{x \to 2} \frac{x^3-8}{x-2}",
    r"\lim_{x \to 0} \frac{\sqrt{x+1}-1}{x}",
    r"\lim_{x \to 0} \frac{\ln(x+1)}{x}",
    r"\lim_{x \to 0} \frac{\sin(2x)}{x}",
    r"\lim_{x \to 3} \frac{x^2-9}{x-3}",
]

answers = ["7", "0", "1", "0", "2", "1", "11", "0", "Pas de limite", "0", "1", "Pas de limite", "4", "0", "1/2", "12", "1/2", "1", "2", "6"]

# 💾 Initialisation session state
if "show_quiz2" not in st.session_state:
    st.session_state.show_quiz2 = False
if "quiz2_score" not in st.session_state:
    st.session_state.quiz2_score = 0
if "niveau" not in st.session_state:
    st.session_state.niveau = ""
if "show_score2" not in st.session_state:
    st.session_state.show_score2 = False

responses = []
st.header("Répondez aux 20 questions :")

for i, q in enumerate(questions):
    st.latex(q)
    rep = st.text_input(f"Réponse {i+1} :", key=f"q_{i}")
    responses.append(rep.strip())

# ✅ Soumettre Quiz 1
if st.button("✅ Soumettre mes réponses"):
    score = 0
    for user_ans, correct_ans in zip(responses, answers):
        if user_ans.lower() == correct_ans.lower():
            score += 1

    total = len(questions)
    pourcentage = (score / total) * 100

    st.subheader("🎯 Résultat du Quiz")
    st.write(f"Votre score est **{score}/{total}** soit **{pourcentage:.2f}%**")
    st.progress(int(pourcentage))

    # Déterminer niveau et afficher Quiz 2
    st.session_state.show_quiz2 = True
    st.session_state.show_score2 = False  # reset score affichage
    if pourcentage >= 80:
        st.session_state.niveau = "avancé"
        st.session_state.exercices2 = [
            (r"\lim_{x \to 3} \frac{x^3 - 27}{x - 3}", "27"),
            (r"\lim_{x \to 0} \frac{\sqrt{x^2 + 4} - 2}{x}", "0"),
            (r"\lim_{x \to 0} \frac{e^x - e^{-x}}{2x}", "1"),
            (r"\lim_{x \to 2} \frac{x^4 - 16}{x^2 - 4}", "4"),
            (r"\lim_{x \to 0} \frac{\ln(1 + x^2)}{x^2}", "0"),
        ]
    elif pourcentage >= 50:
        st.session_state.niveau = "moyen"
        st.session_state.exercices2 = [
            (r"\lim_{x \to 3} \frac{x^2 - 9}{x - 3}", "6"),
            (r"\lim_{x \to 2} \frac{x^2 - 4}{x - 2}", "4"),
            (r"\lim_{x \to 0} \frac{1 - \cos(x)}{x^2}", "0.5"),
            (r"\lim_{x \to 0} \frac{\sin(x)}{x}", "1"),
            (r"\lim_{x \to 0} \frac{\tan(x)}{x}", "1"),
        ]
    else:
        st.session_state.niveau = "débutant"
        st.session_state.exercices2 = [
            (r"\lim_{x \to 1} (2x + 1)", "3"),
            (r"\lim_{x \to 2} x^2", "4"),
            (r"\lim_{x \to 0} \frac{\sin(x)}{x}", "1"),
            (r"\lim_{x \to \infty} \frac{1}{x}", "0"),
            (r"\lim_{x \to 0} e^x", "1"),
        ]

# ➡️ Quiz 2 : Toujours affiché si activé
if st.session_state.show_quiz2:
    st.header("📚 Nouveaux exercices recommandés")
    st.info(f"Niveau recommandé : **{st.session_state.niveau.capitalize()}**")

    score2 = 0
    for i, (q2, rep2) in enumerate(st.session_state.exercices2):
        st.latex(q2)
        user2 = st.text_input(f"Réponse exercice {i+1} :", key=f"q2_{i}")
        if user2.lower() == rep2.lower():
            score2 += 1

    st.session_state.quiz2_score = score2

    # Bouton "Voir mon score"
    if st.button("🎯 Voir mon score"):
        st.session_state.show_score2 = True

    # Afficher le score SEULEMENT après clic
    if st.session_state.show_score2:
        st.success(f"🎉 Ton score est : {score2} / {len(st.session_state.exercices2)}")
        if score2 >= int(len(st.session_state.exercices2) * 0.8):
            st.balloons()
