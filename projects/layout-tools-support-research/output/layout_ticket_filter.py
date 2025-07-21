import pandas as pd
import re
import os
from bs4 import BeautifulSoup
import glob

def extract_tickets_from_html(html_file_path):
    """Extract ticket data from HTML files containing support ticket information"""
    tickets = []
    
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Parse HTML
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all rows with ticket data
    rows = soup.find_all('tr')
    
    current_category = None
    current_occurrences = None
    current_overview = None
    
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 4:
            # Check if this is a category header row
            if cells[0].get_text().strip() and cells[1].get_text().strip().isdigit():
                current_category = cells[0].get_text().strip()
                current_occurrences = cells[1].get_text().strip()
                current_overview = cells[2].get_text().strip()
            
            # Check if this is a case row (has URL)
            case_text = cells[3].get_text().strip()
            if case_text and 'https://wix.wixanswers.com' in case_text:
                # Extract ticket URL
                url_pattern = r'https://wix\.wixanswers\.com/app/helpdesk/ticket/([a-f0-9-]+)'
                url_match = re.search(url_pattern, case_text)
                
                if url_match:
                    ticket_url = url_match.group(0)
                    ticket_id = url_match.group(1)
                    
                    # Extract case description (text before the URL)
                    description = case_text.split('[https://')[0].strip()
                    
                    # Clean up description
                    description = re.sub(r'^Case \d+:\s*', '', description)
                    description = description.rstrip(' .')
                    
                    tickets.append({
                        'ticket_id': ticket_id,
                        'ticket_url': ticket_url,
                        'category': current_category,
                        'total_occurrences': current_occurrences,
                        'category_overview': current_overview,
                        'description': description,
                        'source_file': os.path.basename(html_file_path)
                    })
    
    return tickets

def calculate_layout_relevance_score(row):
    """Calculate confidence score (1-10) for how relevant a ticket is to layout issues"""
    
    # Define layout-related keywords with different weights
    high_priority_keywords = [
        'layout', 'grid', 'section', 'cell', 'resize', 'sizing', 'align', 'spacing', 
        'position', 'responsive', 'mobile', 'breakpoint', 'overlap', 'stack', 'column', 
        'row', 'margin', 'padding', 'width', 'height', 'container', 'flexbox'
    ]
    
    medium_priority_keywords = [
        'design', 'structure', 'arrange', 'organize', 'display', 'view', 'screen', 
        'tablet', 'desktop', 'adjust', 'move', 'shift', 'placement', 'visual'
    ]
    
    layout_specific_terms = [
        'section grid', 'repeater', 'layout tools', 'cell size', 'grid template',
        'responsive design', 'viewport', 'breakpoint management', 'mobile view',
        'alignment', 'white space', 'element positioning'
    ]
    
    # Get text to analyze (description + category + overview)
    text = (
        (row['description'] or '') + ' ' + 
        (row['category'] or '') + ' ' + 
        (row['category_overview'] or '')
    ).lower()
    
    score = 0
    
    # Check for layout-specific terms (high weight)
    for term in layout_specific_terms:
        if term.lower() in text:
            score += 3
    
    # Check for high priority keywords
    for keyword in high_priority_keywords:
        if keyword in text:
            score += 2
    
    # Check for medium priority keywords  
    for keyword in medium_priority_keywords:
        if keyword in text:
            score += 1
    
    # Category-based scoring
    category_lower = (row['category'] or '').lower()
    if any(term in category_lower for term in ['grid', 'layout', 'responsive', 'sizing', 'spacing']):
        score += 3
    
    # Source file bonus (repeater and section grid files are highly relevant)
    source_file = (row['source_file'] or '').lower()
    if 'grid' in source_file or 'repeater' in source_file:
        score += 2
    
    # Cap the score at 10
    final_score = min(10, score)
    
    # Ensure minimum score of 1 if there's any layout relevance
    if final_score > 0 and final_score < 3:
        final_score = max(3, final_score)
    
    return final_score

def main():
    # Get all HTML files in the research directory
    html_files = glob.glob('projects/layout-tools-support-research/context/Research for Eilam/*.html')
    
    all_tickets = []
    
    # Process each HTML file
    for html_file in html_files:
        print(f"Processing {html_file}...")
        tickets = extract_tickets_from_html(html_file)
        all_tickets.extend(tickets)
    
    # Create DataFrame
    df = pd.DataFrame(all_tickets)
    
    if df.empty:
        print("No tickets found!")
        return
    
    # Calculate layout relevance scores
    df['layout_relevance_score'] = df.apply(calculate_layout_relevance_score, axis=1)
    
    # Filter for layout-relevant tickets (score >= 3)
    layout_tickets = df[df['layout_relevance_score'] >= 3].copy()
    
    # Sort by relevance score (highest first) then by category
    layout_tickets = layout_tickets.sort_values(['layout_relevance_score', 'category'], ascending=[False, True])
    
    # Select and rename columns for final output
    output_columns = {
        'ticket_id': 'Ticket_ID',
        'ticket_url': 'Ticket_URL', 
        'description': 'Issue_Description',
        'category': 'Category',
        'layout_relevance_score': 'Layout_Relevance_Score_1_to_10',
        'source_file': 'Data_Source'
    }
    
    final_df = layout_tickets[list(output_columns.keys())].rename(columns=output_columns)
    
    # Save to CSV
    output_file = 'projects/layout-tools-support-research/output/filtered_layout_issues.csv'
    final_df.to_csv(output_file, index=False)
    
    # Print summary statistics
    print(f"\n=== LAYOUT ISSUES FILTERING RESULTS ===")
    print(f"Total tickets processed: {len(df)}")
    print(f"Layout-relevant tickets (score ≥ 3): {len(layout_tickets)}")
    print(f"Filtered CSV saved to: {output_file}")
    
    print(f"\n=== SCORE DISTRIBUTION ===")
    score_dist = layout_tickets['layout_relevance_score'].value_counts().sort_index()
    for score, count in score_dist.items():
        print(f"Score {score}: {count} tickets")
    
    print(f"\n=== TOP CATEGORIES ===")
    category_counts = layout_tickets['category'].value_counts().head(10)
    for category, count in category_counts.items():
        print(f"{category}: {count} tickets")

if __name__ == "__main__":
    main() 