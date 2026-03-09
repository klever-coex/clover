#include <nodelet/nodelet.h>
#include <pluginlib/class_list_macros.h>

#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <cv_bridge/cv_bridge.h>

#include <opencv2/opencv.hpp>

class ImageProxyNodelet : public nodelet::Nodelet
{
private:
  ros::Subscriber sub_;
  ros::Publisher pub_;

public:

  virtual void onInit()
  {
    ros::NodeHandle& nh  = getNodeHandle();
    ros::NodeHandle& pnh = getPrivateNodeHandle();

    std::string input_topic;
    std::string output_topic;

    pnh.param<std::string>("input", input_topic, "image_in");
    pnh.param<std::string>("output", output_topic, "image_out");

    pub_ = nh.advertise<sensor_msgs::Image>(output_topic, 1);
    sub_ = nh.subscribe(input_topic, 1, &ImageProxyNodelet::cb, this);

    NODELET_INFO("ImageProxyNodelet initialized");
  }

  void cb(const sensor_msgs::ImageConstPtr& msg)
  {
    try
    {
      cv_bridge::CvImageConstPtr cv_ptr =
        cv_bridge::toCvShare(msg, msg->encoding);

      cv::Mat img = cv_ptr->image;

      cv_bridge::CvImage out;
      out.header = msg->header;
      out.encoding = msg->encoding;
      out.image = img;

      pub_.publish(out.toImageMsg());
    }
    catch (cv_bridge::Exception& e)
    {
      NODELET_ERROR("cv_bridge exception: %s", e.what());
    }
  }
};

PLUGINLIB_EXPORT_CLASS(ImageProxyNodelet, nodelet::Nodelet)
