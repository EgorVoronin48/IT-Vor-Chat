import sqlite3
from datetime import datetime, timedelta
from typing import Dict, Optional, List


async def save_answers(user_id: int, answers: Dict, survey_type: str) -> bool:

    try:
        with sqlite3.connect("bd/tg.db") as conn:
            cursor = conn.cursor()

            if survey_type == 'self':
                cursor.execute('''
                    INSERT OR REPLACE INTO survey 
                    (user_id, color, food, film, music, yeartime, 
                     drink, rest, animal, holiday, sport)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    user_id,
                    answers.get('color'),
                    answers.get('food'),
                    answers.get('film'),
                    answers.get('music'),
                    answers.get('yeartime'),
                    answers.get('drink'),
                    answers.get('rest'),
                    answers.get('animal'),
                    answers.get('holiday'),
                    answers.get('sport')
                ))
            else:
                cursor.execute('''
                    INSERT OR REPLACE INTO friend_answers 
                    (user_id, friend_id, color, food, film, music, 
                     yeartime, drink, rest, animal, holiday, sport)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    user_id,
                    answers.get('friend_id'),
                    answers.get('color'),
                    answers.get('food'),
                    answers.get('film'),
                    answers.get('music'),
                    answers.get('yeartime'),
                    answers.get('drink'),
                    answers.get('rest'),
                    answers.get('animal'),
                    answers.get('holiday'),
                    answers.get('sport')
                ))

            conn.commit()
            return True

    except sqlite3.Error as e:
        print(f"Database error in save_answers: {e}")
        return False


async def get_user_stats(user_id: int) -> List[Dict]:
    try:
        with sqlite3.connect("bd/tg.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute('''
                SELECT s.match_percent, u.first_name as friend_name, 
                       s.test_date as date
                FROM stats s
                JOIN users u ON s.friend_id = u.user_id
                WHERE s.user_id = ?
                ORDER BY s.test_date DESC
                LIMIT 10
            ''', (user_id,))

            return [dict(row) for row in cursor.fetchall()]

    except sqlite3.Error as e:
        print(f"Database error in get_user_stats: {e}")
        return []


async def calculate_match(user_id: int, friend_id: int, answers: Dict = None) -> Optional[float]:
    try:
        with sqlite3.connect("bd/tg.db") as conn:
            cursor = conn.cursor()

            if answers is None:
                cursor.execute('''
                    SELECT color, food, film, music, yeartime,
                           drink, rest, animal, holiday, sport
                    FROM friend_answers
                    WHERE user_id = ? AND friend_id = ?
                ''', (user_id, friend_id))
                user_answers = cursor.fetchone()
            else:
                fields_order = [
                    'color', 'food', 'film', 'music', 'yeartime',
                    'drink', 'rest', 'animal', 'holiday', 'sport'
                ]
                user_answers = tuple(answers.get(field) for field in fields_order)

            cursor.execute('''
                SELECT color, food, film, music, yeartime,
                       drink, rest, animal, holiday, sport
                FROM survey
                WHERE user_id = ?
            ''', (friend_id,))
            friend_answers = cursor.fetchone()

            if not user_answers or not friend_answers:
                return None

            percent = 0.0
            for u, f in zip(user_answers, friend_answers):
                if u is not None and f is not None:
                    if u == f:
                        percent += 10

            percent = min(percent, 100.0)

            test_date = datetime.now()

            cursor.execute('''
                            INSERT INTO stats (user_id, friend_id, match_percent, test_date)
                            VALUES (?, ?, ?, ?)
                        ''', (user_id, friend_id, percent, test_date))
            conn.commit()

            return percent

    except sqlite3.Error as e:
        print(f"Database error in calculate_match: {e}")
        return None


async def reset_user_survey(user_id: int) -> bool:

    try:
        with sqlite3.connect("bd/tg.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM survey WHERE user_id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Database error in reset_user_survey: {e}")
        return False


async def get_correct_answers(user_id: int, friend_id: int) -> Dict:
    try:
        with sqlite3.connect("bd/tg.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute('''
                SELECT color, food, film, music, yeartime,
                       drink, rest, animal, holiday, sport
                FROM survey
                WHERE user_id = ?
            ''', (friend_id,))
            friend_answers = cursor.fetchone()

            cursor.execute('''
                SELECT color, food, film, music, yeartime,
                       drink, rest, animal, holiday, sport
                FROM friend_answers
                WHERE user_id = ? AND friend_id = ?
            ''', (user_id, friend_id))
            user_answers = cursor.fetchone()

            if not friend_answers or not user_answers:
                return {}

            return {
                'user_answers': dict(user_answers),
                'correct_answers': dict(friend_answers)
            }

    except sqlite3.Error as e:
        print(f"Database error in get_correct_answers: {e}")
        return {}