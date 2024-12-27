try:
    from ..utils.db import *
    from ..agent.chat_history import clear_chat_history
    from ..llm_settings import llm_show_name, llm_settings
    from ..audio.tts import is_local_tts_available
    from ..audio.stt import is_local_stt_available

except ImportError:
    from core.utils.db import *
    from core.llm_settings import llm_show_name, llm_settings
    from core.audio.tts import is_local_tts_available
    from core.audio.stt import is_local_stt_available

from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
)
from PyQt5.QtCore import Qt


def llmsettings_popup(self):
    from ..jarvis import the_main_window

    settings_dialog = QDialog()
    settings_dialog.setWindowTitle("Settings")
    settings_dialog.setWindowModality(Qt.ApplicationModal)
    settings_dialog.setLayout(QVBoxLayout())

    api_key_label = QLabel("OpenAI API Key")
    settings_dialog.layout().addWidget(api_key_label)
    api_key_input = QLineEdit(load_api_key())
    api_key = load_api_key()
    api_key_input.setText(api_key)
    settings_dialog.layout().addWidget(api_key_input)
    save_button = QPushButton("Save")

    nexusai_api_key_label = QLabel("NexusAI  API Key")
    settings_dialog.layout().addWidget(nexusai_api_key_label)
    nexusai_api_key_input = QLineEdit(load_nexusai_api_key())
    nexusai_api_key = load_api_key()
    api_key_input.setText(nexusai_api_key)
    settings_dialog.layout().addWidget(nexusai_api_key_input)
    nexusai_save_button = QPushButton("Save")

    # NexusAI API URL
    nexusai_url_label = QLabel("NexusAI Base URL")
    settings_dialog.layout().addWidget(nexusai_url_label)
    nexusai_url_input = QLineEdit()
    nexusai_url = load_nexusai_url()
    nexusai_url_input.setText(nexusai_url)
    settings_dialog.layout().addWidget(nexusai_url_input)

    def save_nexusai_url_():
        openai_url = nexusai_url_input.text()
        save_nexusai_url(openai_url)
        the_main_window.update_from_thread("Saved NexusAI Base URL")
        the_main_window.input_box.setPlaceholderText("Type here")
        settings_dialog.close()

    nexsai_url_save_button = QPushButton("Save URL")
    nexsai_url_save_button.clicked.connect(save_nexusai_url_)
    settings_dialog.layout().addWidget(nexsai_url_save_button)

    def save_nexusai_api_key_(api_key):
        save_nexusai_api_key(api_key)
        the_main_window.update_from_thread("Saved API Key")
        the_main_window.input_box.setPlaceholderText("Type here")
        settings_dialog.close()

    nexusai_save_button.clicked.connect(lambda: save_nexusai_api_key_(nexusai_api_key_input.text()))
    settings_dialog.layout().addWidget(nexusai_save_button)

    openai_url_label = QLabel("OpenAI Base URL")
    settings_dialog.layout().addWidget(openai_url_label)
    openai_url_input = QLineEdit()
    openai_url = load_openai_url()
    openai_url_input.setText(openai_url)
    settings_dialog.layout().addWidget(openai_url_input)

    def save_openai_url_():
        openai_url = openai_url_input.text()
        save_openai_url(openai_url)
        the_main_window.update_from_thread("Saved OpenAI Base URL")
        the_main_window.input_box.setPlaceholderText("Type here")
        settings_dialog.close()

    openai_url_save_button = QPushButton("Save URL")
    openai_url_save_button.clicked.connect(save_openai_url_)
    settings_dialog.layout().addWidget(openai_url_save_button)


    api_version_label = QLabel("API Version")
    settings_dialog.layout().addWidget(api_version_label)
    api_version_input = QLineEdit()
    api_version = load_api_version()
    api_version_input.setText(api_version)
    settings_dialog.layout().addWidget(api_version_input)

    def save_api_version_():
        api_version = api_version_input.text()
        save_api_version(api_version)
        the_main_window.update_from_thread("Saved API Version")
        the_main_window.input_box.setPlaceholderText("Type here")
        settings_dialog.close()

    api_version_save_button = QPushButton("Save URL")
    api_version_save_button.clicked.connect(save_api_version_)
    settings_dialog.layout().addWidget(api_version_save_button)


    groq_api_key_label = QLabel("Groq API Key")
    settings_dialog.layout().addWidget(groq_api_key_label)
    groq_api_key_input = QLineEdit()
    groq_api_key = load_groq_api_key()
    groq_api_key_input.setText(groq_api_key)
    settings_dialog.layout().addWidget(groq_api_key_input)
    groq_save_button = QPushButton("Save")

    def groq_save_api_key_(api_key):
        save_groq_api_key(api_key)
        the_main_window.update_from_thread("Saved Groq API Key")
        the_main_window.input_box.setPlaceholderText("Type here")
        settings_dialog.close()

    groq_save_button.clicked.connect(
        lambda: groq_save_api_key_(groq_api_key_input.text())
    )
    settings_dialog.layout().addWidget(groq_save_button)

    google_api_key_label = QLabel("Google Generative AI API Key")
    settings_dialog.layout().addWidget(google_api_key_label)
    google_api_key_input = QLineEdit()
    google_api_key = load_google_api_key()
    google_api_key_input.setText(google_api_key)
    settings_dialog.layout().addWidget(google_api_key_input)
    google_save_button = QPushButton("Save")

    def google_save_api_key_(api_key):
        save_google_api_key(api_key)
        the_main_window.update_from_thread("Saved Google API Key")
        the_main_window.input_box.setPlaceholderText("Type here")
        settings_dialog.close()

    google_save_button.clicked.connect(
        lambda: google_save_api_key_(google_api_key_input.text())
    )
    settings_dialog.layout().addWidget(google_save_button)

    def hide_openai():
        api_key_label.hide()
        api_key_input.hide()

        save_button.hide()

    def hide_nexusai():
        nexusai_api_key_label.hide()
        nexusai_api_key_input.hide()
        nexusai_url_label.hide()
        nexusai_url_input.hide()
        nexsai_url_save_button.hide()
        nexusai_save_button.hide()

    def hide_azureai():
        api_key_label.hide()
        api_key_input.hide()
        save_button.hide()
        openai_url_label.hide()
        openai_url_input.hide()
        openai_url_save_button.hide()
        api_version_label.hide()
        api_version_input.hide()
        api_version_save_button.hide()
        

    def hide_groq():
        groq_api_key_label.hide()
        groq_api_key_input.hide()
        groq_save_button.hide()

    def hide_google():
        google_api_key_label.hide()
        google_api_key_input.hide()
        google_save_button.hide()

    def show_openai():
        api_key_label.show()
        api_key_input.show()
        save_button.show()

    def show_azureai():
        api_key_label.show()
        api_key_input.show()
        save_button.show()
        openai_url_label.show()
        openai_url_input.show()
        openai_url_save_button.show()
        api_version_label.show()
        api_version_input.show()
        api_version_save_button.show()

    def show_groq():
        groq_api_key_label.show()
        groq_api_key_input.show()
        groq_save_button.show()

    def show_google():
        google_api_key_label.show()
        google_api_key_input.show()
        google_save_button.show()
    def show_nexusai():
        nexusai_api_key_label.show()
        nexusai_api_key_input.show()
        nexusai_url_label.show()
        nexusai_url_input.show()
        nexsai_url_save_button.show()
        nexusai_save_button.show()

    hide_openai()
    hide_azureai()
    hide_groq()
    hide_google()
    hide_nexusai()

    model_label = QLabel("Model")
    model_select = QComboBox()
    list_of_llm=list(llm_show_name.keys())
    model_select.addItems(list_of_llm)
    settings_dialog.layout().addWidget(model_label)
    settings_dialog.layout().addWidget(model_select)

    current_model = load_model_settings()
    for i, model in enumerate(llm_show_name.keys()):
        if llm_show_name[model] == current_model:
            model_select.setCurrentIndex(i)

    if llm_settings[llm_show_name[model_select.currentText()]]["provider"] == "openai":
        show_openai()
    if llm_settings[llm_show_name[model_select.currentText()]]["provider"] == "NexusAI":
        show_nexusai()
    if llm_settings[llm_show_name[model_select.currentText()]]["provider"] == "azureai":
        show_azureai()

    
    if llm_settings[llm_show_name[model_select.currentText()]]["provider"] == "groq":
        show_groq()
    if llm_settings[llm_show_name[model_select.currentText()]]["provider"] == "google":
        show_google()

    if not llm_settings[llm_show_name[model_select.currentText()]]["vision"]:
        the_main_window.remove_screenshot_button()

    def on_model_change():
        hide_openai()
        hide_azureai()
        hide_groq()
        hide_google()
        the_save_string = llm_show_name[model_select.currentText()]
        save_model_settings(the_save_string)

        if (
            llm_settings[llm_show_name[model_select.currentText()]]["provider"]
            == "openai"
        ):
            show_openai()

        if (
            llm_settings[llm_show_name[model_select.currentText()]]["provider"]
            == "anthropic"
        ):
            show_openai()

        if (
            llm_settings[llm_show_name[model_select.currentText()]]["provider"]
            == "azureai"
        ):
            show_azureai()

        if (
            llm_settings[llm_show_name[model_select.currentText()]]["provider"]
            == "azureopenai"
        ):
            show_openai()
            openai_url_label.show()
            openai_url_input.show()
            openai_url_save_button.show()

        if llm_settings[llm_show_name[model_select.currentText()]]["vision"]:
            the_main_window.add_screenshot_button()
        else:
            the_main_window.remove_screenshot_button()
        if (
            llm_settings[llm_show_name[model_select.currentText()]]["provider"]
            == "groq"
        ):
            show_groq()
        if (
            llm_settings[llm_show_name[model_select.currentText()]]["provider"]
            == "google"
        ):
            show_google()
        if (
            llm_settings[llm_show_name[model_select.currentText()]]["provider"]
            == "nexusai"
        ):
            show_nexusai()

    model_select.currentIndexChanged.connect(on_model_change)

    def add_model_selection(label_text, model_list, current_model, show_model_callback, save_model_callback,
                            availability_check, unavailable_message, layout):
        model_label = QLabel(label_text)
        model_select = QComboBox()
        model_select.addItems(model_list)
        layout.addWidget(model_label)
        layout.addWidget(model_select)

        if current_model in model_list:
            model_select.setCurrentIndex(model_list.index(current_model))
            show_model_callback(current_model)

        def on_model_change():
            selected_model = model_select.currentText()
            show_model_callback(selected_model)
            save_model_callback(selected_model)

        if not availability_check():
            info_text = QLabel(unavailable_message)
            layout.addWidget(info_text)
            model_select.setEnabled(False)

        model_select.currentIndexChanged.connect(on_model_change)
        return model_select

    # Add TTS Model Selection
    add_model_selection(
        label_text="TTS Model",
        model_list=["openai", "microsoft_local", "NexusAI","System"],
        current_model=load_tts_model_settings(),
        show_model_callback=lambda model: show_openai() if model == "openai" else show_nexusai(),
        save_model_callback=save_tts_model_settings,
        availability_check=is_local_tts_available,
        unavailable_message="Please install gpt-computer-assistant[local_tts] to use local TTS",
        layout=settings_dialog.layout(),
    )

    # Add STT Model Selection
    add_model_selection(
        label_text="STT Model",
        model_list=["openai", "openai_whisper_local", "NexusAI"],
        current_model=load_stt_model_settings(),
        show_model_callback=lambda model: show_openai() if model == "openai" else show_nexusai(),
        save_model_callback=save_stt_model_settings,
        availability_check=is_local_stt_available,
        unavailable_message="Please install gpt-computer-assistant[local_stt] to use local STT",
        layout=settings_dialog.layout(),
    )

    settings_dialog.exec_()

