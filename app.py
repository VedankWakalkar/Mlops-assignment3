from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import matplotlib.pyplot as plt
import os

app = FastAPI()

df = pd.read_csv("./Iris.csv")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

# IrisDataFilter class to filter data based on species
class IrisDataFilter:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def filter_by_species(self, species: str):
        if species not in self.dataframe['Species'].unique():
            raise HTTPException(status_code=404, detail="Species not found")

        filtered_df = self.dataframe[self.dataframe['Species'] == species]
        return filtered_df


def create_feature_visualization(data, species):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle(f"Feature Distributions for {species}")

    features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

    for idx, feature in enumerate(features):
        ax = axes[idx // 2, idx % 2]
        ax.hist(data[feature], bins=20, alpha=0.7, color='blue', edgecolor='black')
        ax.set_title(f'Distribution of {feature}')
        ax.set_xlabel(feature)
        ax.set_ylabel('Frequency')

    # Save the plot as an image file
    image_path = f"static/images/{species}.png"
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(image_path)
    plt.close()

    return image_path

@app.get("/", response_class="html")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/filter-data")
async def filter_iris_data(request: Request, species: str, page: int = Query(1, ge=1)):

    iris_filter = IrisDataFilter(df)
    filtered_df = iris_filter.filter_by_species(species)

    # Pagination logic (10 rows per page)
    rows_per_page = 10
    start_idx = (page - 1) * rows_per_page
    end_idx = start_idx + rows_per_page
    total_pages = (len(filtered_df) + rows_per_page - 1) // rows_per_page
    paginated_data = filtered_df.iloc[start_idx:end_idx]

    image_path = create_feature_visualization(filtered_df, species)

    return templates.TemplateResponse("filtered_data.html", {
        "request": request,
        "filtered_data": paginated_data.to_dict(orient="records"),
        "species": species,
        "image": f"/{image_path}",
        "current_page": page,
        "total_pages": total_pages
    })
