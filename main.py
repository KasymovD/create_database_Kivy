from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Create A Table
        c.execute("""CREATE TABLE if not exists customers(
            name text)
        """)

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

        return Builder.load_file('first_db.kv')

    # def on_start(self):
    #     self.root.ids.tabs.add_widget(Tab(title=f"Tab"))
    #     self.root.ids.tabs.add_widget(Tab(title=f"Tab 2"))

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        instance_tab.ids.label.text = tab_text

    def submit(self):
        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Add A Record
        c.execute("INSERT INTO customers VALUES (:first)",
            {
                'first': self.root.ids.word_input.text,
            })

        # Add a little message
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

    def show_record (self):

        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Grab records from database
        c.execute("SELECT * FROM customers")
        records = c.fetchall()

        word = ''
        # Loop thru records
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text = f'{word}'

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()



MainApp().run()