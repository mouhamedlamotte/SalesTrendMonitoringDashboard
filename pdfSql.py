from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Bulletin Q - Reporting des ventes', border=0, ln=1, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, border=0, ln=1, align='L')
        self.ln(5)

    def chapter_description(self, desc):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, desc)
        self.ln(5)

    def add_visualization_placeholder(self, title):
        self.chapter_title(title)
        self.set_fill_color(200, 200, 200)  # Gray placeholder
        self.cell(0, 50, 'Visualisation ici', border=1, ln=1, fill=True)
        self.ln(10)

# Création du PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Page de couverture
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Bulletin Q - [Période : Mois, Année]', border=0, ln=1, align='C')
pdf.ln(20)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, "Ce document présente une analyse des performances des ventes pour la période donnée. Il inclut des indicateurs clés, des visualisations et des recommandations stratégiques.")
pdf.ln(20)

# Table des matières
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Table des matières', border=0, ln=1, align='L')
pdf.ln(10)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, """1. Résumé exécutif
2. Analyse des performances mensuelles
3. Analyse des performances trimestrielles
4. Comparaison annuelle
5. Visualisations et tendances clés
6. Conclusion et recommandations""")
pdf.ln(10)

# Section 1: Résumé exécutif
pdf.add_page()
pdf.chapter_title("1. Résumé exécutif")
pdf.chapter_description(
    "Cette section fournit un aperçu rapide des indicateurs clés de la période, y compris le chiffre d'affaires, le volume des transactions, et les produits ou régions les plus performants."
)
pdf.add_visualization_placeholder("Visualisation : Indicateurs clés (Donut chart)")

# Section 2: Analyse des performances mensuelles
pdf.chapter_title("2. Analyse des performances mensuelles")
pdf.chapter_description(
    "Analyse des ventes et des tendances pour le mois en cours, incluant l'évolution des ventes et la répartition par catégorie ou région."
)
pdf.add_visualization_placeholder("Visualisation : Évolution quotidienne des ventes (Line chart)")
pdf.add_visualization_placeholder("Visualisation : Répartition des ventes par catégorie (Bar chart)")

# Section 3: Analyse des performances trimestrielles
pdf.chapter_title("3. Analyse des performances trimestrielles")
pdf.chapter_description(
    "Présentation des performances au cours du trimestre, avec une comparaison des mois précédents pour identifier les tendances clés."
)
pdf.add_visualization_placeholder("Visualisation : Parts de marché par catégorie (Stacked bar chart)")
pdf.add_visualization_placeholder("Visualisation : Activité par jour et heure (Heat map)")

# Section 4: Comparaison annuelle
pdf.chapter_title("4. Comparaison annuelle")
pdf.chapter_description(
    "Comparaison des performances de la période actuelle avec celles de l'année précédente pour évaluer les progrès et identifier les écarts."
)
pdf.add_visualization_placeholder("Visualisation : Évolution annuelle des ventes (Line chart)")
pdf.add_visualization_placeholder("Visualisation : Répartition annuelle par catégorie (Treemap)")

# Section 5: Visualisations et tendances clés
pdf.chapter_title("5. Visualisations et tendances clés")
pdf.chapter_description(
    "Section dédiée aux visualisations supplémentaires pour approfondir l'analyse des données et identifier les opportunités cachées."
)
pdf.add_visualization_placeholder("Visualisation : Répartition des ventes par région (Region map)")
pdf.add_visualization_placeholder("Visualisation : Mots-clés ou marques populaires (Tag cloud)")

# Section 6: Conclusion et recommandations
pdf.chapter_title("6. Conclusion et recommandations")
pdf.chapter_description(
    "Résumé des points clés du trimestre, avec des recommandations pour améliorer les performances futures et des prévisions pour la période à venir."
)

# Sauvegarde
pdf.output('Bulletin_Q_Reporting.pdf')
